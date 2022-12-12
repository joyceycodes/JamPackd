from fastapi.testclient import TestClient
from queries.playlists import PlaylistQueries
from main import app
from authenticator_music import authenticate

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_all_playlists(self, user_id):
        return []

    def get_playlist(self, playlist_id, user_id):
        return {
            "id": 1,
            "name": "string",
            "songs": [{"name": "string", "artist": "string", "uri": "string"}],
            "comments": "string",
        }

    def delete_playlist(self, id):
        return True


def test_get_all_playlists():
    # Arrange
    account = {"id": 123}
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    app.dependency_overrides[
        authenticate.get_current_account_data
    ] = lambda: account

    # Act
    response = client.get("/api/playlists")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"playlists": []}

    # Clean up
    app.dependency_overrides = {}


def test_get_playlist():
    expected = {
        "id": 1,
        "name": "string",
        "songs": [{"name": "string", "artist": "string", "uri": "string"}],
        "comments": "string",
    }
    # Arrange
    account = {"id": 123}
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    app.dependency_overrides[
        authenticate.get_current_account_data
    ] = lambda: account

    # Act
    response = client.get("/api/playlists/1")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected

    # Clean up
    app.dependency_overrides = {}


def test_delete_playlist():

    account = {"id": 123}
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    response = client.get("/api/playlists")
    app.dependency_overrides[
        authenticate.get_current_account_data
    ] = lambda: account

    response = client.delete("api/playlists/1")

    assert response.status_code == 200
    assert response.json() == {"playlists": []}
    assert response.json() == True  # noqa

    app.dependency_overrides = {}
