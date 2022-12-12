from fastapi.testclient import TestClient
from queries.playlists import PlaylistQueries
from authenticator_music import authenticate
from main import app

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_all_playlists(self):
        return []

    def delete_playlist(self, id):

        return True


# def test_get_all_playlists():
#     app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
#     response = client.get("/api/playlists")
#     assert response.status_code == 200
#     assert response.json() == {"playlists": []}

#     app.dependency_overrides = {}


def test_delete_playlist():

def test_get_all_playlists():
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    response = client.get("/api/playlists")
    assert response.status_code == 200
    assert response.json() == {"playlists": []}


