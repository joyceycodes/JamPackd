import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from fastapi import APIRouter
import os


router = APIRouter(tags=["spotify"])


@router.post("/recommendations")
def get_recommendations(request: dict):
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
        )
    )

    genre = list(request["genre"].split())

    data = sp.recommendations(seed_genres=genre, limit=50)
    recommendations = []
    for idx, track in enumerate(data["tracks"]):
        recommendations.append(
            {
                "uri": track["uri"].split("track:", 1)[1],
                "name": track["name"],
                "artist": track["artists"][0]["name"],
            }
        )
    return recommendations


# user ID needed to create playlist
@router.get("/user")
def get_user():
    sp_oauth = create_spotify_oauth()
    user = spotipy.Spotify(oauth_manager=sp_oauth).current_user()
    return user["id"]


@router.get("/login")
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return auth_url


@router.post("/music/playlist")
def authorize(response):
    sp_oauth = create_spotify_oauth()
    # session.clear()
    code = response.split("code=", 1)[1]
    # code = f"http://localhost:3000/music/playlist?code={response}"
    token_info = sp_oauth.get_access_token(code)
    print(token_info, code)
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        redirect_uri=os.environ["REDIRECT_URI"],
        scope="playlist-modify-private playlist-modify-public",
    )


def create_playlist():
    sp_oauth = create_spotify_oauth()

    playlist = spotipy.Spotify(oauth_manager=sp_oauth).user_playlist_create(
        get_user(),
        "Jam Pack'd Playlist 2",
        public=True,
        description="",
    )

    return playlist


@router.post("/playlist")
def update_playlist(uris):
    uris = [
        "spotify:track:5Z3GHaZ6ec9bsiI5BenrbY",
    ]
    sp_oauth = create_spotify_oauth()
    playlist = create_playlist()

    results = spotipy.Spotify(oauth_manager=sp_oauth).user_playlist_add_tracks(
        playlist["owner"]["id"],
        playlist_id=playlist["id"],
        tracks=uris,
    )
    return results
