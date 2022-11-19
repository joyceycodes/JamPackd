from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries
from pydantic import BaseModel

router = APIRouter()


class Song(BaseModel):
    id: str
    name: str
    artist: str
    uri: str


class Playlist(BaseModel):
    id: int
    name: str
    songs: list[Song]
    playlist_id: str


class PlaylistIn(BaseModel):
    id: int
    name: str
    songs: list[Song]


class PlaylistsOut(BaseModel):
    playlists: list[Playlist]


class PlaylistOut(BaseModel):
    id: int | str
    name: str
    songs: list[Song]


# get all playlists
@router.get("/api/playlists/", response_model=PlaylistsOut)
def get_all_playlists(queries: PlaylistQueries = Depends()):
    return {
        "playlists": queries.get_all_playlists(),
    }


# get playlist by ID
@router.get("/api/playlists/{id}", response_model=Playlist)
def get_playlist(
    playlist_id: str,
    response: Response,
    queries: PlaylistQueries = Depends(),
):
    record = queries.get_playlist(playlist_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/playlists/", response_model=PlaylistOut)
def create_playlist(
    playlist_in: PlaylistIn, queries: PlaylistQueries = Depends()
):
    return queries.create_playlist(playlist_in)


@router.get("/api/recommendations/")
def get_recommendations():
    # import requests
    pass
