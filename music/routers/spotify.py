# import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import keys
import sys

from fastapi import APIRouter
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


router = APIRouter()


@router.get("/api/recommendations/")
def get_recommendations():
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=keys.client_ID, client_secret=keys.client_SECRET
        )
    )

    if len(sys.argv) > 1:
        seed_genre = sys.argv[1]
    else:
        seed_genre = ["country"]

    data = sp.recommendations(seed_genres=seed_genre, limit=10)
    sanitized = sanitize_songs(data)

    return sanitized

    # for idx, track in enumerate(data["tracks"]):
    #     print(idx, "NAME:", track["name"])
    #     print("URI:", track["uri"])
    #     print("ARTIST:", track["artists"][0]["name"])


def sanitize_songs(data):
    sanitized_song = [
        #     id:
        #     name:
        #     artist:
        #     uri:
    ]
    #

    for idx, track in enumerate(data["tracks"]):
        res = data.get(["id", "name", "artist", "uri"])

        sanitized_song.append(res)

        # print(idx, "NAME:", track["name"])
        # print("URI:", track["uri"])
        # print("ARTIST:", track["artists"][0]["name"])
    return sanitized_song


@router.post("/api/create_spotify_playlist/")
def create_spotify_playlist():

    scope = ["playlist-modify-private", "playlist-modify-public"]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=keys.client_ID,
            client_secret=keys.client_SECRET,
            redirect_uri=keys.redirect_uri,
            scope=scope,
        )
    )

    pl_name = input("Enter Playlist Name: ")

    result = sp.user_playlist_create(
        keys.user, pl_name, public=False, collaborative=True, description=""
    )

    return result["id"]


@router.post("/api/update_spotify_playlist/")
def update_spotify_playlist():
    uris = ["spotify:track:1LDeuD3jbSpHucsd0nOt6t"]
    scope = ["playlist-modify-private", "playlist-modify-public"]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=keys.client_ID,
            client_secret=keys.client_SECRET,
            redirect_uri=keys.redirect_uri,
            scope=scope,
        )
    )

    results = sp.user_playlist_add_tracks(
        keys.user, playlist_id="3AUA37TYmufE9fVyrwz8aW", tracks=uris
    )
