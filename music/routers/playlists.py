from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries
from queries.spotify import SpotifyQueries

# from routers import keys
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
import os

import json
import requests

from requests_oauthlib import OAuth2Session

from requests.auth import HTTPBasicAuth

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
# from .songs import Song
from pydantic import BaseModel


router = APIRouter()


class Song(BaseModel):
    id: str
    name: str
    artist: str
    uri: str


class Recommendations(BaseModel):
    recommendations: list[Song]


class PlaylistIn(BaseModel):
    id: str
    name: str
    songs: list[Song]
    ext_url: str


class PlaylistOut(BaseModel):
    id: int | str
    name: str
    songs: list[Song]
    ext_url: str


class PlaylistsOut(BaseModel):
    playlists: list[PlaylistOut]


# get all playlists
@router.get("/api/playlists/", response_model=PlaylistsOut)
def get_all_playlists(queries: PlaylistQueries = Depends()):
    playlists = []
    for playlist in queries.get_all_playlists():
        playlist["id"] = str(playlist["_id"])
        playlists.append(playlist)
    return {"playlists": playlists}


# get playlist by ID
@router.get("/api/playlists/{playlist_id}", response_model=PlaylistOut)
def get_playlist(
    playlist_id: str,
    response: Response,
    queries: PlaylistQueries = Depends(),
):
    record = queries.get_playlist(playlist_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/playlists/", response_model=PlaylistOut)
def create_playlist(
    playlist_in: PlaylistIn, queries: PlaylistQueries = Depends()
):
    return queries.create_playlist(playlist_in)


@router.delete("/api/playlists/{playlist_id}", response_model=bool)
def delete_playlist(playlist_id: str, queries: PlaylistQueries = Depends()):
    queries.delete_playlist(playlist_id)
    return True


@router.put("/api/playlists/{playlist_id}", response_model=PlaylistOut)
def update_playlist(
    # playlist_id: str,
    playlist: PlaylistIn,
    queries: PlaylistQueries = Depends(),
):
    return queries.update_playlist(playlist)


@router.get("/api/spotify/recommendations/")
def get_recommendations(
    queries: SpotifyQueries = Depends(),
):
    return queries.get_recommendations(["pop"])


@router.post("/api/spotify/get_token")
def get_token():
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    redirect_uri = os.environ["REDIRECT_URL"]

    authorization_base_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"
    scope = ["playlist-modify-private", "playlist-modify-public"]

    spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

    # Redirect user to Spotify for authorization
    authorization_url, state = spotify.authorization_url(
        authorization_base_url
    )
    print("Please go here and authorize: ", authorization_url)

    # Get the authorization verifier code from the callback url
    redirect_response = redirect_uri

    auth = HTTPBasicAuth(client_id, client_secret)

    # Fetch the access token
    token = spotify.fetch_token(
        token_url,
        auth=auth,
        authorization_response=redirect_response,
    )

    print(token)
    return token


# Fetch a protected resource, i.e. user profile
# auth_url = "https://accounts.spotify.com/api/token"
# data = {
#     "grant_type": "client_credentials",
#     "client_id": keys.client_ID,
#     "client_secret": keys.client_SECRET,
#     # "scope": ["playlist-modify-private", "playlist-modify-public"],
#     # "redirect_uri": keys.redirect_uri,
# }
# auth_response = requests.post(auth_url, data=data)
# access_token = auth_response.json().get("access_token")
# print(access_token)
# return access_token


@router.post("/api/spotify/create/")
def create_sp_playlist(
    # playlist=Depends(create_playlist),
):
    token = ""
    print(token)
    user_id = "1254524921"
    print(user_id)
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps(
        {
            "name": "Indie bands like Franz Ferdinand but using Python",
            "description": "My first programmatic playlist, yooo!",
            "public": False,
        }
    )
    response = requests.post(
        url=endpoint_url,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token),
        },
    )
    print(response)
    return True


# @router.post("/api/spotify/update/")
# def update_sp_playlist(
#     queries: SpotifyQueries = Depends(),
# ):
#     return queries.update_sp_playlist()

# import random
# import math
# import base64
# from fastapi.responses import RedirectResponse, HTMLResponse
# from urllib.parse import urlencode

# STATE_KEY = "spotify_auth_state"
# CLIENT_ID = keys.client_ID
# CLIENT_SECRET = keys.client_SECRET
# URI = keys.redirect_uri
# REDIRECT_URI = URI + "/callback"


# def generate_random_string(string_length):
#     possible = "ABCDEFGHI789"
#     text = "".join(
#         [
#             possible[math.floor(random.random() * len(possible))]
#             for i in range(string_length)
#         ]
#     )

#     return text


# @router.get("/login")
# def read_root(response: Response):
#     state = generate_random_string(20)

#     scope = "playlist-modify-private playlist-modify-public"

#     params = {
#         "response_type": "code",
#         "client_id": CLIENT_ID,
#         "scope": scope,
#         "redirect_uri": REDIRECT_URI,
#         "state": state,
#     }
#     response = RedirectResponse(
#         url="https://accounts.spotify.com/authorize?" + urlencode(params)
#     )
#     response.set_cookie(key=STATE_KEY, value=state)
#     return response


# @router.get("/callback")
# def callback(request: Request, response: Response):

#     code = request.query_params["code"]
#     state = request.query_params["state"]
#     stored_state = request.cookies.get(STATE_KEY)

#     if state == None or state != stored_state:
#         raise HTTPException(status_code=400, detail="State mismatch")
#     else:

#         response.delete_cookie(STATE_KEY, path="/", domain=None)

#         url = "https://accounts.spotify.com/api/token"
#         request_string = CLIENT_ID + ":" + CLIENT_SECRET
#         encoded_bytes = base64.b64encode(request_string.encode("utf-8"))
#         encoded_string = str(encoded_bytes, "utf-8")
#         header = {"Authorization": "Basic " + encoded_string}

#         form_data = {
#             "code": code,
#             "redirect_uri": REDIRECT_URI,
#             "grant_type": "authorization_code",
#         }

#         api_response = requests.post(url, data=form_data, headers=header)

#         if api_response.status_code == 200:
#             data = api_response.json()
#             access_token = data["access_token"]
#             refresh_token = data["refresh_token"]

#             response = RedirectResponse(url=URI)
#             response.set_cookie(key="accessToken", value=access_token)
#             response.set_cookie(key="refreshToken", value=refresh_token)

#         return response


# @router.get("/refresh_token")
# def refresh_token(request: Request):

#     refresh_token = request.query_params["refresh_token"]
#     request_string = CLIENT_ID + ":" + CLIENT_SECRET
#     encoded_bytes = base64.b64encode(request_string.encode("utf-8"))
#     encoded_string = str(encoded_bytes, "utf-8")
#     header = {"Authorization": "Basic " +
# encoded_string}

#     form_data = {"grant_type":
# "refresh_token", "refresh_token": refresh_token}

#     url = "https://accounts.spotify.com/api/token"

#     response = requests.post(url, data=form_data, headers=header)
#     if response.status_code != 200:
#         raise HTTPException
# (status_code=400, detail="Error with refresh token")
#     else:
#         data = response.json()
#         access_token = data["access_token"]

#         return {"access_token": access_token}
