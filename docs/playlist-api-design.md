### Create new playlist

* Endpoint path: /api/playlists/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request body:

    ```json
    {
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
    ```


* Response shape:

    ```json
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
    ```

### List all playlists

* Endpoint path: /api/playlists/
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

* Endpoint path: /api/playlists/{playlist_id}
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request body:

    ```json
  {
  "comments": "string",
  "name": "string"
  }
    ```

* Response: A list of playlists
* Response shape:

    ```json
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
    ```

### Delete playlist 

* Endpoint path: /api/playlists/{playlist_id}
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response shape:

    ```json
   true
    ```
