### November 22, 2022
- Group programming to get the Update Playlist endpoint working, with help from James
- Created a gmail and Spotify account for our project with Tiffany
- Pair programming with Tiffany. We were able to make successful requests using Spotipy to create and update a playlist, which was such an AHA! moment. We ran into an obstacle where we would try to create a playlist on our group account, but getting a 403 error that said the User was not autherized with our app. The fix was for Tiffany to restart her computer (which restarted the session?) and grant autherization for our app to make changes on our group Spotify account. Now need to get it working with FastAPI.
- The way it works with the Spotify API, each user needs to autherize our app (Jam Pack'd) to make changes on their Spotify account. This would drastically limit the usage of our app to only Spotify users. I'm thinking the best option is to create and update playlists on our group account, so that way the only account that needs to be autherized is our group Spotify account. Hopefully the option for the user to autherize us if they wanted to will be something we'll be able to implement. Still unsure how to make sure that it's always our group account that is being used to create and update playlists. 

### November 21, 2022
Today I worked on:
- Pair programming with Tiffany to get the Songs endpoints that she worked on connected to Mongo. James came and had some suggestions for our back end design. He suggested that we may not need endpoints for Songs afterall but that having the pydantic model for Song will still be helpful to make sure the shape of the data is correct. Scrapped all the endpoints that we had for Songs.
- Worked with Spotipy API. I was able to get some data using their search functions that does not require user authentication. Am still working on getting track recommendations. 
- Will need to figure out how to use their authenticated endpoints as well. It's slightly more complex in that it requires a redirect uri and a spotify username.

### November 18, 2022
Today I worked on:
- Group programming to get the Create and Get Account by ID endpoint running
- Solidified backend design with the inclusion of a songs model
- Learned that the songs can be related to the playlists by creating a songs attribute in the Playlist model with the value list[Song]
- Learned that the unique identifier created by MongoDB for each model instance is an ObjectID type, not a string
- Got the Create Playlist endpoint working but still working on getting the Get and Get All endpoints working. Running into a type error.

### November 17, 2022
Today I worked on:
- Created a diagram that navigated through the user's experience and the corresponding HTTP requests
- Group programming to start on the FastAPI endpoints for new users with MongoDB, endpoints are still not showing up on the docs page yet
- Talked to Shahzad who wants to see more CRUD functionality on our site. Discussed adding possible features such as a comment/thought section for each playlist, allowing users to rate a song or playlist, or implementing a poller that polls the for the top songs from spotify on a periodic basis.
    - I like the idea of having songs saved in our database as it would protect us in case anything went wrong with the Spotify API and using a poller would satisfy CRUD requirements. Updating our database with new sonds and deleting songs that havent been accessed in while.
- Played around with OAuth token and was able to make successful GET requests for track recommendations. The caveat is that the token only lasts a short amount of time so will need to find a workaround. Exploring Spotipy as a possible option. 

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