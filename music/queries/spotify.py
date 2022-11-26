import os
import pymongo

# from bson.objectId import ObjectId
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from routers import keys

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]

mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)

genres = [
    "acoustic",
    "afrobeat",
    "alt-rock",
    "alternative",
    "ambient",
    "anime",
    "black-metal",
    "bluegrass",
    "blues",
    "bossanova",
    "brazil",
    "breakbeat",
    "british",
    "cantopop",
    "chicago-house",
    "children",
    "chill",
    "classical",
    "club",
    "comedy",
    "country",
    "dance",
    "dancehall",
    "death-metal",
    "deep-house",
    "detroit-techno",
    "disco",
    "disney",
    "drum-and-bass",
    "dub",
    "dubstep",
    "edm",
    "electro",
    "electronic",
    "emo",
    "folk",
    "forro",
    "french",
    "funk",
    "garage",
    "german",
    "gospel",
    "goth",
    "grindcore",
    "groove",
    "grunge",
    "guitar",
    "happy",
    "hard-rock",
    "hardcore",
    "hardstyle",
    "heavy-metal",
    "hip-hop",
    "holidays",
    "honky-tonk",
    "house",
    "idm",
    "indian",
    "indie",
    "indie-pop",
    "industrial",
    "iranian",
    "j-dance",
    "j-idol",
    "j-pop",
    "j-rock",
    "jazz",
    "k-pop",
    "kids",
    "latin",
    "latino",
    "malay",
    "mandopop",
    "metal",
    "metal-misc",
    "metalcore",
    "minimal-techno",
    "movies",
    "mpb",
    "new-age",
    "new-release",
    "opera",
    "pagode",
    "party",
    "philippines-opm",
    "piano",
    "pop",
    "pop-film",
    "post-dubstep",
    "power-pop",
    "progressive-house",
    "psych-rock",
    "punk",
    "punk-rock",
    "r-n-b",
    "rainy-day",
    "reggae",
    "reggaeton",
    "road-trip",
    "rock",
    "rock-n-roll",
    "rockabilly",
    "romance",
    "sad",
    "salsa",
    "samba",
    "sertanejo",
    "show-tunes",
    "singer-songwriter",
    "ska",
    "sleep",
    "songwriter",
    "soul",
    "soundtracks",
    "spanish",
    "study",
    "summer",
    "swedish",
    "synth-pop",
    "tango",
    "techno",
    "trance",
    "trip-hop",
    "turkish",
    "work-out",
    "world-music",
]


class SpotifyQueries:
    def get_recommendations(self, genre):
        sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=keys.client_ID, client_secret=keys.client_SECRET
            )
        )
        # if genre in genres:
        data = sp.recommendations(seed_genres=genre, limit=20)
        recommendations = []
        for idx, track in enumerate(data["tracks"]):
            recommendations.append(
                {
                    "uri": track["uri"],
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                }
            )
        return recommendations

    # def create_sp_playlist(self, pl_name):
    #     scope = ["playlist-modify-private", "playlist-modify-public"]

    #     sp = spotipy.Spotify(
    #         auth_manager=SpotifyOAuth(
    #             client_id=keys.client_ID,
    #             client_secret=keys.client_SECRET,
    #             redirect_uri=keys.redirect_uri,
    #             scope=scope,
    #         )
    #     )

    #     playlist = sp.user_playlist_create(
    #         keys.user,
    #         pl_name,
    #         public=True,
    #         collaborative=True,
    #         description="",
    #     )
    #     print("AAAAAAAA", playlist["id"])
    #     return playlist["id"]

    # def update_sp_playlist(self):
    #     uris = ["spotify:track:1LDeuD3jbSpHucsd0nOt6t"]
    #     scope = ["playlist-modify-private", "playlist-modify-public"]

    #     sp = spotipy.Spotify(
    #         auth_manager=SpotifyOAuth(
    #             client_id=keys.client_ID,
    #             client_secret=keys.client_SECRET,
    #             redirect_uri=keys.redirect_uri,
    #             scope=scope,
    #         )
    #     )

    #     results = sp.user_playlist_add_tracks(
    #         keys.user, playlist_id="5BDwuYuDuwVrsLSzSvX5wF", tracks=uris
    #     )

    #     return True
