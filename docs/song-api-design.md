
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
