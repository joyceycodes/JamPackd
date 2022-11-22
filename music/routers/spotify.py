# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import keys
import sys

# scope = "user-read-recently-played"

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         client_id=keys.client_ID,
#         client_secret=keys.client_SECRET,
#         redirect_uri=keys.redirect_url,
#         scope=scope,
#     )
# )


# def getSongs():
#     results = sp.current_user_recently_played()
#     for idx, item in enumerate(results["items"]):
#         track = item["track"]
#         print(idx, track["artists"][0]["name"], " – ", track["name"])


# print(getSongs())


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=keys.client_ID, client_secret=keys.client_SECRET
    )
)

# results = sp.search(q="weezer", limit=20)
# for idx, track in enumerate(results["tracks"]["items"]):
#     print(idx, track["name"])

# playlists = sp.user_playlists("spotify")
# while playlists:
#     for i, playlist in enumerate(playlists["items"]):
#         print(
#             "%4d %s %s"
#             % (i + 1 + playlists["offset"], playlist["uri"], playlist["name"])
#         )
#     if playlists["next"]:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

if len(sys.argv) > 1:
    seed_genre = sys.argv[1]
else:
    seed_genre = "country"

results = sp.recommendations(seed_genres=seed_genre)
for idx, track in enumerate(results["tracks"]["items"]):
    print(idx, track["name"])
