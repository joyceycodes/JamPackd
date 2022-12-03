# *****************************************************
# USING SPOTIPY
# *****************************************************

# def create_playlist():
#     scope = ["playlist-modify-private", "playlist-modify-public"]
#     print("*********** HERE")

#     sp = spotipy.Spotify(
#         auth_manager=SpotifyOAuth(
#             client_id=keys.client_ID,
#             client_secret=keys.client_SECRET,
#             redirect_uri=keys.redirect_uri,
#             scope=scope,
#         )
#     )
#     print("***********", sp)
#     print(keys.client_SECRET)
#     playlist = sp.user_playlist_create(
#         keys.user,
#         "pl_name",
#         public=False,
#         collaborative=True,
#         description="",
#     )
#     # print("AAAAAAAA", playlist["id"])
#     print(playlist)
#     return playlist

# @router.post("/api/spotify/update/")
# def update_sp_playlist(
#     queries: SpotifyQueries = Depends(),
# ):
#     return queries.update_sp_playlist()

# *****************************************************
# USING SPOTIFY API / REQUESTS
# *****************************************************

# from requests.auth import HTTPBasicAuth
# from requests_oauthlib import OAuth2Session
# from routers import keys
# from requests_oauthlib import OAuth2Session

# client_id = keys.client_ID
# client_secret = keys.client_SECRET
# redirect_uri = keys.redirect_uri
# # @router.post("/api/spotify/get_token")

# # get authorization from user
# def get_auth_url():

#     authorization_base_url =
# "https://accounts.spotify.com/authorize"
#     token_url = "https://accounts.spotify.com/api/token"

#     scope = ["playlist-modify-private", "playlist-modify-public"]

#     spotify = OAuth2Session(client_id, scope=scope,
# redirect_uri=redirect_uri)

#     # Redirect user to Spotify for authorization
#     authorization_url, state = spotify.authorization_url(
#         authorization_base_url
#     )
#     # separate function that returns url
#     print(authorization_url)
#     return authorization_url


# get_auth_url()
# # from requests.auth import HTTPBasicAuth

# # # "window.location = url" in the frontend to redirect
# # create endpoint
# # fast api with automagically parse the queries,
# # will set code to the value we need


# @router.get("/api/spotifytoken")
# def fetch_token_using_redirect(code):
#     # Get the authorization verifier code from the callback url
#     redirect_response =
# f"https://jampackd-music.onrender.com/?code={code}"

#     token_url = "https://accounts.spotify.com/api/token"
#     scope = ["playlist-modify-private", "playlist-modify-public"]
#     auth = HTTPBasicAuth(client_id, client_secret)
#     spotify = OAuth2Session(client_id, scope=scope,
# redirect_uri=redirect_uri)
#     # Fetch the access token
#     token = spotify.fetch_token(
#         token_url, auth=auth,
# authorization_response=redirect_response
#     )

#     return token["access_token"]


# import json
# import requests

# # @router.post("/api/spotify/create/")
# def create_sp_playlist(
#     # playlist=Depends(create_playlist),
# ):
#     token = get_token()
#     print(token)
#     user_id = "31gv6grbwedyw3u7fxfucsuvq7ua"
#     endpoint_url =
# f"https://api.spotify.com/v1/users/{user_id}/playlists"
#     request_body = json.dumps(
#         {
#             "name": "Testing Test",
#             "description": "My first programmatic
# playlist, yooo!",
#             "public": False,
#         }
#     )
#     response = requests.post(
#         url=endpoint_url,
#         data=request_body,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": "Bearer {}".format(token),
#         },
#     )
#     print(response)
#     return response


# create_sp_playlist()


# *****************************************************
# USING SPOTIFY API / FASTAPI SAMPLE FROM GITHUB
# https://github.com/duranbe/spotify-fastapi-sample
# *****************************************************

# from routers import keys
# import random
# import math
# import base64
# from fastapi.responses import RedirectResponse, HTMLResponse
# from urllib.parse import urlencode
# from fastapi import Response, Request, HTTPException
# import requests


# STATE_KEY = "spotify_auth_state"
# CLIENT_ID = keys.client_ID
# CLIENT_SECRET = keys.client_SECRET
# URI = keys.redirect_uri
# REDIRECT_URI = URI + "/callback"


# def generate_random_string(string_length):
#     possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZa
#   bcdefghijklmnopqrstuvwxyz0123456789"
#     text = "".join(
#         [
#             possible[math.floor(random.random() *
#  len(possible))]
#             for i in range(string_length)
#         ]
#     )
#     return text


# # @router.get("/login")
# def read_root(response: Response):
#     state = generate_random_string(16)

#     scope = "playlist-modify-private playlist-modify-public"

#     params = {
#         "response_type": "code",
#         "client_id": CLIENT_ID,
#         "scope": scope,
#         "redirect_uri": REDIRECT_URI,
#         "state": state,
#     }
#     response = RedirectResponse(
#         url="https://accounts.spotify.com/authorize?"
# + urlencode(params)
#     )
#     response.set_cookie(key=STATE_KEY, value=state)
#     return response


# read_root()

# # @router.get("/callback")
# def callback(request: Request, response: Response):

#     code = request.query_params["code"]
#     state = request.query_params["state"]
#     stored_state = request.cookies.get(STATE_KEY)

#     if state == None or state != stored_state:
#         raise HTTPException(status_code=400,
# detail="State mismatch")
#     else:

#         response.delete_cookie(STATE_KEY, path="/", domain=None)

#         url = "https://accounts.spotify.com/api/token"
#         request_string = CLIENT_ID + ":" + CLIENT_SECRET
#         encoded_bytes =
# base64.b64encode(request_string.encode("utf-8"))
#         encoded_string = str(encoded_bytes, "utf-8")
#         header = {"Authorization": "Basic " + encoded_string}

#         form_data = {
#             "code": code,
#             "redirect_uri": REDIRECT_URI,
#             "grant_type": "authorization_code",
#         }

#         api_response = requests.post(url, data=form_data,
# headers=header)

#         if api_response.status_code == 200:
#             data = api_response.json()
#             access_token = data["access_token"]
#             refresh_token = data["refresh_token"]

#             response = RedirectResponse(url=URI)
#             response.set_cookie(key="accessToken",
# value=access_token)
#             response.set_cookie(key="refreshToken",
# value=refresh_token)

#         return response


# # @router.get("/refresh_token")
# def refresh_token(request: Request):

#     refresh_token = request.query_params["refresh_token"]
#     request_string = CLIENT_ID + ":" + CLIENT_SECRET
#     encoded_bytes =
# base64.b64encode(request_string.encode("utf-8"))
#     encoded_string = str(encoded_bytes, "utf-8")
#     header = {"Authorization": "Basic " + encoded_string}

#     form_data = {"grant_type": "refresh_token",
# "refresh_token": refresh_token}

#     url = "https://accounts.spotify.com/api/token"

#     response = requests.post(url, data=form_data, headers=header)
#     if response.status_code != 200:
#         raise HTTPException(status_code=400,
# detail="Error with refresh token")
#     else:
#         data = response.json()
#         access_token = data["access_token"]

#         return {"access_token": access_token}
