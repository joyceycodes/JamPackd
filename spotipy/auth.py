import spotipy
import key
from spotipy.oauth2 import SpotifyOAuth


scope = ["playlist-modify-private", "playlist-modify-public"]
uris = [
    "spotify:track:1LDeuD3jbSpHucsd0nOt6t",
    "spotify:track:3ZXZ9RMsznqgyHnyq0K5FL",
    "spotify:track:215NabWUpxjY9XY8qAZ3zR",
]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=key.client_ID,
        client_secret=key.client_SECRET,
        redirect_uri=key.redirect_url,
        scope=scope,
    )
)
# seed_genre = ["country", "opera", "ska", "rap"]
# data = sp.recommendations(seed_genres=seed_genre, limit=8)
# # print(data)

# for idx, track in enumerate(data["tracks"]):
#     print(idx, "TITLE:", track["name"])
#     print("URI:", track["uri"])
#     print("ARTIST:", track["artists"][0]["name"])


def create_playlist():
    pl_name = input("Enter Playlist Name: ")

    # results = sp.user_playlists(key.user_joyce, limit=50, offset=0)

    # create playlist
    results = sp.user_playlist_create(
        key.user, pl_name, public=False, collaborative=True, description=""
    )
    print(results)


def add_to_playlist():

    results = sp.user_playlist_add_tracks(
        key.user, playlist_id="0By2izdMAVY0hiyYOi9SB2", tracks=uris
    )
    print(results)


add_to_playlist()
# # results = sp.user("1254524921")
# print("Results********", results["id"])


# for idx, item in enumerate(results["items"]):
#     track = item["track"]
#     print(idx, track["artists"][0]["name"], " – ", track["name"])

# results = sp.recommendation_genre_seeds()
# print(results)
