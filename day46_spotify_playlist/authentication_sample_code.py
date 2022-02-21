# Examples of implementing the Authorization Code Flow presented on Spotify
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/

# Some good reference
# https://www.youtube.com/watch?v=yAXoOolPvjU
import random
import string
import requests
import webbrowser
from pprint import pprint
import base64

CLIENT_ID = "70d974b67b0e48f289a9a1e14ca45746"
CLIENT_SECRET = "cbce51096469459c9209d8ef8d6ba79c"
REDIRECT_URI = "http://example.com"
SCOPE = "user-library-read, user-library-modify, playlist-modify-private, playlist-read-private, playlist-modify-public"

random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))


def encode_b64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def get_auth_code(client_id, redirect_uri, scope, state):
    AUTH_CODE_URL = "https://accounts.spotify.com/authorize"

    parameters = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": state
    }
    auth_code_response = requests.get(url=AUTH_CODE_URL, params=parameters)
    auth_code_response.raise_for_status()

    # open request url in the browser and get redirect url with code and state
    webbrowser.open(auth_code_response.url)

    redirect_link = input("Copy and paste the redirect link.\n")

    ls = redirect_link.split("=")
    response_data = {}
    # case with code only
    if len(ls) == 2:
        response_data = {"code": ls[1], "state": ""}
    # case with both code and state
    elif len(ls) == 3:
        response_data = {"code": ls[1].split("&")[0], "state": ls[2]}
    else:
        print("error")

    return response_data


def get_access_token(authorization_code, redirect_uri, client_id, client_secret):
    URL = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
    }

    header_auth_str = encode_b64(f"{client_id}:{client_secret}")

    headers = {
        "Authorization": f"Basic {header_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url=URL, data=data, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    pprint(response_data)
    return response_data


def refresh_access_token(refresh_token, client_id, client_secret):
    URL = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    header_auth_str = encode_b64(f"{client_id}:{client_secret}")

    headers = {
        "Authorization": f"Basic {header_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url=URL, data=data, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    pprint(response_data)
    return response_data


# Step 1: Request User Authorization
auth_code = get_auth_code(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE, state=random_string)

# Step 2: Request Access Token
access_token_data = get_access_token(authorization_code=auth_code["code"],
                                     redirect_uri=REDIRECT_URI,
                                     client_id=CLIENT_ID, client_secret=CLIENT_SECRET)


# # Step 3 (Optional): Request Refresh Access Token
# refresh_token_data = refresh_access_token(access_token_data["refresh_token"], CLIENT_ID, CLIENT_SECRET)

# Step 4 : Use the access toke to perform query
# Use search as an example

BASE_URL = "https://api.spotify.com/v1"
search_url = f"{BASE_URL}/search"

parameters = {
    "q": "artist:adele track:hello",
    "type": "track",
    "limit": 1,
    "market": "US"
}

headers = {
    "Authorization": f"Bearer {access_token_data['access_token']}"
}
search_response = requests.get(url=search_url, params=parameters, headers=headers)
search_response.raise_for_status()
print("\nThe search results are below:\n")
pprint(search_response.json())
