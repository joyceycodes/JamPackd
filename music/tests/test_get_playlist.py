from fastapi.testclient import TestClient
from queries.playlists import PlaylistQueries
from main import app
from authenticator_music import authenticate

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_playlist(self, playlist_id, user_id):
        return {
            "id": 1,
            "name": "string",
            "songs": [{"name": "string", "artist": "string", "uri": "string"}],
            "comments": "string",
        }


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