# !!! Environment variables, client ID, secret and redirect url need to be defined.
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
from pprint import pprint


def input_validation(n: int, input_type: str, min_value, max_value):
    """

    Args:
        input_type (): choose from "year", "month" and "date"
        n (): the expected number of the characters in the user input
        min_value ():
        max_value ():

    Returns: the valid user input

    """

    validation_pass = False
    while not validation_pass:
        user_input = input(f"Please enter the {input_type} in {n} digits ({min_value} - {max_value}).\n")
        try:
            if len(user_input) == n:
                num = int(user_input)
                if min_value <= num <= max_value:
                    validation_pass = True
                    return user_input
                else:
                    print("The input is out of range. Please enter again.")
                    validation_pass = False
            else:
                validation_pass = False
                print(f"Please enter the number with {n} digits.")
        except ValueError as ex:
            validation_pass = False
            print(str(ex) + "\n" + "Please make sure to enter an number.\n")


def get_date() -> str:
    """

    Returns: date in string format yyyy-mm-dd

    """
    use_today = input("Do you want to see the latest (up to last week) top 100 hits? Please enter 'Yes' or 'No'.\n")
    if use_today.lower() in ('y', 'yes'):
        date_string = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        year = input_validation(4, "year", 1900, datetime.now().year)
        month = input_validation(2, "month", 1, 12)
        date = input_validation(2, "date", 1, 31)

        date_string = f"{year}-{month}-{date}"
    return date_string


def get_titles(date_string: str) -> list:
    url = f"https://www.billboard.com/charts/hot-100/{date_string}/"
    response = requests.get(url=url)
    response.raise_for_status()
    html_text = response.text

    # one way to get the titles in a list
    soup0 = BeautifulSoup(html_text, "html.parser")
    ls = soup0.find_all("h3", class_="a-no-trucate", id="title-of-a-story")
    titles0 = [h3.text.strip() for h3 in ls]

    # get a list to include both the song title and the artist name
    soup = BeautifulSoup(html_text, 'html.parser')
    # each element in songs_info list is a bs4.element.Tag
    # each tag contains children including a h3 tag with the title and a span tag with the artist name
    songs_info = soup.find_all("li", class_="lrv-u-padding-l-1@mobile-max")
    titles1 = [(soup_tag.h3.text.strip(), soup_tag.span.text.strip()) for soup_tag in songs_info]

    validation_title_list = [single_title[0] for single_title in titles1]

    # validate to make sure lists of the titles are generated correctly
    if len(titles1) == len(titles0) and all(
            [titles0[index] == validation_title_list[index] for index in range(len(titles1))]):
        print(f"Title number: {len(titles1)}\n")
        print("Title list passes the validation.\n")
        return titles1
    else:
        print("Title list does not pass the validation.\n")
        exit()


def get_authentication() -> Spotify:
    # perform oauth2.0 authentication with spotify
    scope = "user-library-read, user-library-modify, playlist-modify-private, playlist-read-private, playlist-modify-public"
    # documentation https://spotipy.readthedocs.io/en/2.19.0/
    # examples on github https://github.com/plamere/spotipy
    spotify = Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return spotify


def check_playlist(spotify: Spotify, playlist_title) -> bool:
    # get basic information about existing playlists and place them in a dictionary
    playlist_dict = {playlist["name"]: [playlist["id"], playlist["uri"]] for playlist in
                     spotify.current_user_playlists()["items"]}

    # check if there is already a playlist created for selected date
    create_new_playlist = False
    if len(playlist_dict) != 0 and playlist_title in playlist_dict.keys():
        print("The playlist is already available.")
    else:
        create_new_playlist = True

    return create_new_playlist


def get_trackIDs(title_ls: list, spotify: Spotify, date_string: str) -> list:
    for title in title_ls:
        # print(title[0], "--", title[1])
        # print(title[0].split("-")[0], "--", title[1])
        result = spotify.search(q=f"track:{title[0].split('-')[0]} year:{date_string.split('-')[0]}", limit=1,
                                type="track", market="US")
        if bool(result["tracks"]["items"]):
            track_ids.append(result["tracks"]["items"][0]["id"])
        else:
            print(f"Fail to add {title[0]} --- {title[1]}")
    return track_ids


# select the date
date_str = get_date()
# create empty list for storing track ids needed for adding tracking into playlist
track_ids = []

# playlist name and placeholders for other information
playlist_name = f"Music Time Machine {date_str}"
playlist_description = ""
playlist_id = ""
playlist_uri = ""

sp = get_authentication()
# get user information
user_info = sp.current_user()
user = user_info["id"]

# testing code
# artist filter only looks at the first author, which could be a problem when there is multiple author
# result = sp.search(q="artist:Bruno track:Tell Me Tomorrow - Part I", limit=1, type="track", market="US")
# pprint(result)
#
# result = sp.search(q="track:Just Can't Win 'em All", limit=1, type="track", market="US")
# pprint(result)

new_playlist = check_playlist(spotify=sp, playlist_title=playlist_name)

if new_playlist:
    titles = get_titles(date_str)
    track_ids = get_trackIDs(title_ls=titles, spotify=sp, date_string=date_str)

    playlist_description = f"Top{len(track_ids)} Billboard Playlist on {date_str}"

    # create a playlist for the user
    playlist = sp.user_playlist_create(user=user, name=playlist_name,
                                       description=playlist_description)
    # update the playlist dictionary to include the newly added playlist
    playlist_id = playlist["id"]
    playlist_uri = playlist["uri"]
    sp.playlist_add_items(playlist_id, track_ids)

pprint(sp.current_user_playlists()["items"])
