from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries
from pydantic import BaseModel
from typing import Optional
from authenticator_music import authenticate

router = APIRouter()


class Song(BaseModel):
    name: str
    artist: str
    uri: str


class PlaylistIn(BaseModel):
    name: str
    songs: list[Song]
    comments: Optional[str] = None


class PlaylistOut(BaseModel):
    id: int | str
    name: str
    songs: list[Song]
    comments: Optional[str] = None


class PlaylistsOut(BaseModel):
    playlists: list[PlaylistOut]


class PlaylistUpdate(BaseModel):
    comments: Optional[str] = None
    name: str


# get all playlists not working currently
@router.get("/api/playlists/", response_model=PlaylistsOut)
def get_all_playlists(
    queries: PlaylistQueries = Depends(),
    account: dict = Depends(authenticate.get_current_account_data),
):
    playlists = []
    for playlist in queries.get_all_playlists(account["id"]):
        playlist["id"] = str(playlist["_id"])
        playlists.append(playlist)
    return {"playlists": playlists}


# get playlist by ID
@router.get("/api/playlists/{playlist_id}", response_model=PlaylistOut)
def get_playlist(
    playlist_id: str,
    response: Response,
    queries: PlaylistQueries = Depends(),
    account: dict = Depends(authenticate.get_current_account_data),
):
    record = queries.get_playlist(playlist_id, account["id"])
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/playlists/", response_model=PlaylistOut)
def create_playlist(
    playlist_in: PlaylistIn,
    queries: PlaylistQueries = Depends(),
    account: dict = Depends(authenticate.get_current_account_data),
):
    return queries.create_playlist(playlist_in, account["id"])


@router.delete("/api/playlists/{playlist_id}", response_model=bool)
def delete_playlist(
    playlist_id: str,
    queries: PlaylistQueries = Depends(),
    account_data: dict = Depends(authenticate.get_current_account_data),
):
    queries.delete_playlist(playlist_id),
    return True


@router.put("/api/playlists/{playlist_id}", response_model=PlaylistOut)
def update_playlist(
    playlist_id: str,
    playlist: PlaylistUpdate,
    queries: PlaylistQueries = Depends(),
    account: dict = Depends(authenticate.get_current_account_data),
):
    return queries.update_playlist(playlist_id, playlist)
