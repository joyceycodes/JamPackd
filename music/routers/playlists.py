from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries

# from .songs import Song
from pydantic import BaseModel


router = APIRouter()


class PlaylistIn(BaseModel):
    name: str
    songs: list[Song]


class PlaylistOut(BaseModel):
    id: int | str
    name: str
    songs: list[Song]


class PlaylistsOut(BaseModel):
    playlists: list[PlaylistOut]


# get all playlists
@router.get("/api/playlists/", response_model=PlaylistsOut)
def get_all_playlists(queries: PlaylistQueries = Depends()):
    playlists = []
    for playlist in queries.get_all_playlists():
        playlist["id"] = str(playlist["_id"])
        playlists.append(playlist)
    return {"playlists": playlists}
    # return {
    #   "playlists": queries.get_all_playlists()
    # }


# get playlist by ID
@router.get("/api/playlists/{playlist_id}", response_model=PlaylistOut)
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
