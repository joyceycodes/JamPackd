### CREATE New Playlist

* Endpoint path: api/playlist
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request body:

    ```json
    {
        "name": "string"
    }
    ```

* Response: An indication of success or failure
* Response shape:

    ```json
   {
  "collaborative": true,
  "description": "string",
  "external_urls": {
    "spotify": "string"
  },
  "followers": {
    "href": "string",
    "total": 0
  },
  "href": "string",
  "id": "string",
  "images": [
    {
      "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
      "height": 300,
      "width": 300
    }
  ],
  "name": "string",
  "owner": {
    "external_urls": {
      "spotify": "string"
    },
    "followers": {
      "href": "string",
      "total": 0
    },
    "href": "string",
    "id": "string",
    "type": "user",
    "uri": "string",
    "display_name": "string"
  },
  "public": true,
  "snapshot_id": "string",
  "tracks": {
    "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
    "items": [
      {}
    ],
    "limit": 20,
    "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "offset": 0,
    "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "total": 4
  },
  "type": "string",
  "uri": "string"

}

    ```

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
      "id": 0,
      "name": "string",
      "songs": [
        {
          "name": "string",
          "artist": "string",
          "uri": "string"
        }
      ],
      "comments": "string"
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

### Delete playlist and song from playlist

* Endpoint path: tunder.com/api/playlists/<int:pk>
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

* Endpoint path: tunder.com/api/playlist/song/<int:pk> or something like tunder.com/api/playlist/like/id
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
