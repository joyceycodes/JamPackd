### November 16, 2022
Today I worked on:
- Collaborated with the group to find resources regarding using the SpotifyAPI. Developed our understanding on which requests we want to to use to get songs from Spotify and create a playlist with Spotify.
    - In our method to get songs from Spotify, still wondering if it's better to do a get request for track recommendations or for playlists from Spotify. Tracks requires more input parameters in the request that allow for filtering for specific songs by genre.
    - When creating a playlist, a post request is needed to create and set the name of the playlist. A spotify ID is required to create a playlist. A second request is required to add items in the playlist. 
    - Still need to consider our backend design on how we want Liked songs to be saved. The goal is for the user to be able to receive a list of the songs in text format after creating the playlist. After learning about MongoDB, the no schema structure seems like it allows us to save items verys easily in the database. Maybe something along the lines of this:
        - collection : user
        - document : list of liked songs
        - each user has it's own collection of documents containing a playlist
- Changed the file structure in the playlists directory. Added a queries and routers directory.

### November 15, 2022
Today I worked on:
- Worked with the group on the Docker Compose file to get all the containers running for the playlists, songs, and accounts microservices.
- Started working on queries for playlists. Created playlists/db.py and playlists/models.py.

We decided on having 3 total microservices. Since songs will all be incoming from a third party API (Spotify), I'm wondering if it's essential for it do have it's own database or if it can be shared with the playlists microservice.

### November 10, 2022
Today I worked on:
- Drafted endpoints for list playlist and update playlist