from fastapi import APIRouter
import os


router = APIRouter(tags=["spotify2"])


from requests_oauthlib import OAuth2Session

from requests.auth import HTTPBasicAuth


@router.post("/music/playlist")
def authorize():
    client_id = (os.environ["CLIENT_ID"],)
    client_secret = (os.environ["CLIENT_SECRET"],)
    redirect_uri = (os.environ["REDIRECT_URI"],)

    authorization_base_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"

    scope = ["playlist-modify-private, playlist-modify-public"]

    spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = spotify.authorization_url(
        authorization_base_url
    )
    print("Please go here and authorize: ", authorization_url)
    redirect_response = input("\n\nPaste the full redirect URL here: ")

    auth = HTTPBasicAuth(client_id, client_secret)

    # Fetch the access token
    token = spotify.fetch_token(
        token_url, auth=auth, authorization_response=redirect_response
    )

    print(token)

    # Fetch a protected resource, i.e. user profile
    r = spotify.get("https://api.spotify.com/v1/me")
    print(r.content)
