import spotipy
import key
from spotipy.oauth2 import SpotifyOAuth


scope = ["playlist-modify-private", "playlist-modify-public"]
uris = ["spotify:track:1LDeuD3jbSpHucsd0nOt6t"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=key.client_ID,
        client_secret=key.client_SECRET,
        redirect_uri=key.redirect_url,
        scope=scope,
    )
)


pl_name = input("Enter Playlist Name: ")

# results = sp.user_playlists(key.user_joyce, limit=50, offset=0)
# results = sp.user_playlist_add_tracks(
#     key.user, playlist_id="3AUA37TYmufE9fVyrwz8aW", tracks=uris
# )


# create playlist
results = sp.user_playlist_create(
    key.user, pl_name, public=False, collaborative=True, description=""
)

# results = sp.user("1254524921")
print("Results********", results["id"])


# for idx, item in enumerate(results["items"]):
#     track = item["track"]
#     print(idx, track["artists"][0]["name"], " – ", track["name"])
