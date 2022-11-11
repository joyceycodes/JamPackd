### List playlists

* Endpoint path: api/playlists
* Endpoint method: GET


* Headers:
    * Authorization: Bearer token

* Response: A list of playlists

* Response shape:

```json 
{
  "playlists": [
    {
        "name": "string",
    }
  ]
}
```

### Update Playlist

* Endpoint path: api/playlist/<int:pk>
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request body:

    ```json
    {
          "username": "string",  
          "playlist_name": "string",
          "song_list" : [
            {
            "song_title": "string",
            "artist": "string",
            "duration": "string"
            }
        ]
    ```

* Response: A list of playlists
* Response shape:

    ```json
    {
      "playlist": [
        {
          "id": "int",
          "username": "string",  
          "playlist_name": "string",
          "song_list" : [
            {
            "song_title": "string",
            "artist": "string",
            "duration": "string"
            }
        }
      ]
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
