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

### Delete playlist and song from playlist

* Endpoint path: tunder.com/api/playlists
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response:
* Response shape:

    ```json
    {
      "playlist": [
        {
          "name": string,
          "id":

          
        }
      ]
    }
    ```

* Endpoint path: tunder.com/api/playlist
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response:
* Response shape:

    ```json
    {
      "song": [
        {
          "name": string,
          "artist": string,
          "duration":string,

### GET Song Details

* Endpoint path: api/song
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):

    ```json
    {
        "song_ID": int,
        "song_name": string,
        "artist_name": string,
        "album_art": img,
        "duration": string
    }
    ```

* Response: song title, artist name
* Response shape (JSON):

    ```json
    {
        "song_ID": int,
        "song_name": string,
        "artist_name": string,
        "album_art": img,
        "duration": string
    }
    ```

### CREATE New Playlist

* Endpoint path: api/playlist
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request body:

    ```json
    {
        "name": string,
        "songs": [
        {
            "song_ID": int,
            "song_name": string,
            "artist_name": string,
            "album_art": img,
            "duration": string
        },
        {
            "song_ID": int,
            "song_name": string,
            "artist_name": string,
            "album_art": img,
            "duration": string
        }]
    }
    ```

        }
      ]
    }
    ```

* Response: An indication of success or failure
* Response shape:

    ```json
    {
        "success": boolean,
        "name": string,
        "songs": [
        {
            "song_ID": int,
            "song_name": string,
            "artist_name": string,
            "album_art": img,
            "duration": string
        },
        {
            "song_ID": int,
            "song_name": string,
            "artist_name": string,
            "album_art": img,
            "duration": string
        }]
    }
    ```
