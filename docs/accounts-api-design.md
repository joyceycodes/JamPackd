### Create user

* Endpoint path: /api/users/{user_id}
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request body:
  ```json
  {
  "full_name": "string",
  "username": "string",
  "password": "string"
  }
  ```

* Response shape:
```json
  {
    "access_token": "string",
    "token_type": "Bearer",
    "account": {
      "id": 0,
      "full_name": "string",
      "username": "string"
    }
  }
```
### Log in

* Endpoint path: /token
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response: Account information and a token
* Response shape (JSON):

    ```json
    {
      "account": {
        "«key»: type»,"
      },
      "token": "string"
    }
    ```

### Log out

* Endpoint path: /token
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):

    ```json
    true
    ```
