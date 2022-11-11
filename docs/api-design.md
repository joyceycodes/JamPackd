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

### Create a new Playlist

* Endpoint path: api/tweets
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