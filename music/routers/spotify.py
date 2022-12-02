import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from fastapi import APIRouter
import os


router = APIRouter(tags=["spotify"])

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


@router.get("/recommendations")
def get_recommendations(genre: str):
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
        )
    )
    if genre in genres:
        genre = [genre]
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


@router.get("/authorize")
def authorize(response):
    sp_oauth = create_spotify_oauth()
    # session.clear()
    code = f"https://jampackd-music.onrender.com/authorize?code={response}"

    token_info = sp_oauth.get_access_token(code)
    # session["token_info"] = token_info
    print(token_info)
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
        "Jam Pack'd Playlist",
        public=True,
        description="",
    )

    return playlist


@router.post("/playlist")
def update_playlist():
    uris = [
        "spotify:track:40FLJc17FMZaPmCQEEZgB0",
    ]
    sp_oauth = create_spotify_oauth()
    playlist = create_playlist()

    results = spotipy.Spotify(oauth_manager=sp_oauth).user_playlist_add_tracks(
        playlist["owner"]["id"],
        playlist_id=playlist["id"],
        tracks=uris,
    )
    return results
