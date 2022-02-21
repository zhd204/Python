import string
import random

from bs4 import BeautifulSoup
import requests


# response = requests.get("https://www.billboard.com/charts/hot-100/2022-01-12")
#
# soup = BeautifulSoup(response.text, 'html.parser')
# songs_info = soup.find_all("li", class_="lrv-u-padding-l-1@mobile-max")
# print(len(songs_info))
# print(songs_info[0].h3.text.strip())
# print(songs_info[0].span.text.strip())
#
# print(songs_info[0].name)
# print(songs_info[0].contents[1].text.strip())

# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# scope = "user-library-read, user-library-modify"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#
import base64
CLIENT_ID = "70d974b67b0e48f289a9a1e14ca45746"
CLIENT_SECRET = "cbce51096469459c9209d8ef8d6ba79c"
message = f"{CLIENT_ID}:{CLIENT_SECRET}"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(message_bytes)
print(base64_bytes)
print(base64_message)
