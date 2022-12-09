from fastapi.testclient import TestClient
from accounts.main import app
from authenticator import UserAuthenticator
from accounts.queries import users


client = TestClient(app)

dummy = {
    "email": "email@email.com",
    "password": "password",
    "username": "username",
}

fakeAccStatus = {"success": True}


def test_create_account():
    class fakeAccQuery:
        def create(self, item, item2):
            pass

    app.dependency_overrides[users] = fakeAccQuery

    response = client.post("/api/accounts", json=dummy)
    assert response.status_code == 200
    assert response.json() == fakeAccStatus

    app.dependency_overrides = {}


# def test_duplicate_account():
#     class fakeDuplicateAccQuery:
#         def create(self, item, item2):
#             raise users

#     app.dependency_overrides[AccountQueries] = fakeDuplicateAccQuery

#     response = client.post("/api/accounts", json=fakeAcc)
#     assert response.status_code == 400
#     assert response.json() == {
#         "detail": "Cannot create an account with those credentials"
#     }

#     app.dependency_overrides = {}
