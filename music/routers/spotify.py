# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
# import keys
# import sys

# from fastapi import APIRouter
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials


# router = APIRouter()

# genres = [
#     "acoustic",
#     "afrobeat",
#     "alt-rock",
#     "alternative",
#     "ambient",
#     "anime",
#     "black-metal",
#     "bluegrass",
#     "blues",
#     "bossanova",
#     "brazil",
#     "breakbeat",
#     "british",
#     "cantopop",
#     "chicago-house",
#     "children",
#     "chill",
#     "classical",
#     "club",
#     "comedy",
#     "country",
#     "dance",
#     "dancehall",
#     "death-metal",
#     "deep-house",
#     "detroit-techno",
#     "disco",
#     "disney",
#     "drum-and-bass",
#     "dub",
#     "dubstep",
#     "edm",
#     "electro",
#     "electronic",
#     "emo",
#     "folk",
#     "forro",
#     "french",
#     "funk",
#     "garage",
#     "german",
#     "gospel",
#     "goth",
#     "grindcore",
#     "groove",
#     "grunge",
#     "guitar",
#     "happy",
#     "hard-rock",
#     "hardcore",
#     "hardstyle",
#     "heavy-metal",
#     "hip-hop",
#     "holidays",
#     "honky-tonk",
#     "house",
#     "idm",
#     "indian",
#     "indie",
#     "indie-pop",
#     "industrial",
#     "iranian",
#     "j-dance",
#     "j-idol",
#     "j-pop",
#     "j-rock",
#     "jazz",
#     "k-pop",
#     "kids",
#     "latin",
#     "latino",
#     "malay",
#     "mandopop",
#     "metal",
#     "metal-misc",
#     "metalcore",
#     "minimal-techno",
#     "movies",
#     "mpb",
#     "new-age",
#     "new-release",
#     "opera",
#     "pagode",
#     "party",
#     "philippines-opm",
#     "piano",
#     "pop",
#     "pop-film",
#     "post-dubstep",
#     "power-pop",
#     "progressive-house",
#     "psych-rock",
#     "punk",
#     "punk-rock",
#     "r-n-b",
#     "rainy-day",
#     "reggae",
#     "reggaeton",
#     "road-trip",
#     "rock",
#     "rock-n-roll",
#     "rockabilly",
#     "romance",
#     "sad",
#     "salsa",
#     "samba",
#     "sertanejo",
#     "show-tunes",
#     "singer-songwriter",
#     "ska",
#     "sleep",
#     "songwriter",
#     "soul",
#     "soundtracks",
#     "spanish",
#     "study",
#     "summer",
#     "swedish",
#     "synth-pop",
#     "tango",
#     "techno",
#     "trance",
#     "trip-hop",
#     "turkish",
#     "work-out",
#     "world-music",
# ]


# @router.get("/api/recommendations/")
# def get_recommendations(genre):
#     sp = spotipy.Spotify(
#         auth_manager=SpotifyClientCredentials(
#             client_id=keys.client_ID, client_secret=keys.client_SECRET
#         )
#     )
#     if genre in genres:
#         seed_genre = genre
#     data = sp.recommendations(seed_genres=seed_genre, limit=20)
#     return data

#     # for idx, track in enumerate(data["tracks"]):
#     #     print(idx, "NAME:", track["name"])
#     #     print("URI:", track["uri"])
#     #     print("ARTIST:", track["artists"][0]["name"])


# # def sanitization(data):
# #     data = data["tracks"]


# def sanitize_songs(data):
#     sanitized_songs = [
#         {  #     id:
#             #     name:
#             #     artist:
#             #     uri:
#         },
#         {},
#     ]
#     #
#     for idx, track in enumerate(data["tracks"]):
#         res = data.get(["id", "name", "artist", "uri"])
#         sanitized_songs.append(res)

#         # print(idx, "NAME:", track["name"])
#         # print("URI:", track["uri"])
#         # print("ARTIST:", track["artists"][0]["name"])
#     return sanitized_songs


# def liked_songs(data):
#     # json data gets passed in
#     # declare playlist as an empty list
#     playlist = []

#     # for track in data["tracks"]
#     #   if used clicks like
#     #   filter data
#     #   append tracks["uri"], track["name"], track["artists"]
# [0]["name"] as an object to playlist
#     pass


# # @router.post("/api/create_spotify_playlist/")
# # def create_spotify_playlist():

# #     scope = ["playlist-modify-private", "playlist-modify-public"]

# #     sp = spotipy.Spotify(
# #         auth_manager=SpotifyOAuth(
# #             client_id=keys.client_ID,
# #             client_secret=keys.client_SECRET,
# #             redirect_uri=keys.redirect_uri,
# #             scope=scope,
# #         )
# #     )

# #     pl_name = input("Enter Playlist Name: ")

# #     result = sp.user_playlist_create(
# #         keys.user, pl_name, public=False, c
# ollaborative=True, description=""
# #     )

# #     return result["id"]


# # @router.post("/api/update_spotify_playlist/")
# # def update_spotify_playlist():
# #     uris = ["spotify:track:1LDeuD3jbSpHucsd0nOt6t"]
# #     scope = ["playlist-modify-private", "playlist-modify-public"]

# #     sp = spotipy.Spotify(
# #         auth_manager=SpotifyOAuth(
# #             client_id=keys.client_ID,
# #             client_secret=keys.client_SECRET,
# #             redirect_uri=keys.redirect_uri,
# #             scope=scope,
# #         )
# #     )

# #     results = sp.user_playlist_add_tracks(
# #         keys.user, playlist_id="3AUA37TYmufE9fVyrwz8aW", tracks=uris
# #     )
