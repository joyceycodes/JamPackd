### December 5, 2022

- Worked on the 'Export to Spotify' button. Still unable to get it to work. I originally wanted to have the button navigate to the Spotify auth page, create a playlist, and then redirect back to our site. I'm having trouble with my function that gets the access token after the redirect and receive a 422 unprocessable entity error. After talking to Cam about it, it seems that my backend function to get the access token isn't working right either! I was under the assumption that I needed the code from the redirect uri to get the access token, but even without inputting in a valid code to my function, it still returns an access token. We tried to find where the token in being stored, but didn't find it anywhere in the session storage or cookies. It even worked in incognito mode in the browser which made things more interesting. I think the answer is somewhere within the Spotipy docs but since this has taken me so much time already, I think it's my time is best spent working on getting our MVP done. It is very likely being cached, because after clearing browser cahce, it requires reauthorization with Spotify.
- Worked on the player component on the front end. Tiffany already created a nice looking component with the Like and skip buttons. I'm passing the songs from the Recommendations component as props to the Player component. We need to show each song individually and move on to the next song once the user selects like or skip. Was able to get that working but creating a piece of State that updates onClick for the skip and like buttons. Need to save the liked songs in a list to be able to make a POST request on the next component.

### December 2, 2022

- Created button that exports to the authorization page with Spotify. This will be added to the playlist detail page. It goes to the right page right now but I'm not too sure how to extract the code from the redirect url to be used to make our requests.
- Added authorization to the music microservice for the backend. Created a new authenticator file that had all the jwtdown-fastapi authenticator functions. Then added a dependency for token data in each of the playlist endpoints.
- Added a comments option to the playlists model. I originally thought the comments would need full CRUD, but it seems like a better idea to just add it as an attribute of the playlist since all comments will be connected to one playlist only.

### December 1, 2022

- Got all the spotify endpoints working using Spotipy. I like using Spotipy's library more than Requests-OAuthlib because the code is a lot cleaner. Andrew came and went over the multiple steps for OAuth and it really helped to fill in some missing pieces. The piece I was missing was updating the redirect_uri to be the same as our endpoint for the authorization function. As well as extracting the code query from the redirect url. It's working on the backend, but I think it will still be a challenge to get this going on the front end.
- Created a new router for all the Spotify endpoints for better organization and imported to main.py.
- Updated our api keys in the .env file with Tiffany. We ended up making all the variables in uppercase to prevent confusion. May need to get this update on render too.
- Finished the front end page that gets user input to start music exploration. I created a react component that receives the genre from the user and fetches the recommendations from spotify via our music microservice. We receive the list of songs as a response and need to store that in state somewhere and send it over to a component that will display the Spotify iFrame player.
- Worked with Tiffany to refactor the routes in App.js and Nav.js.

### November 30, 2022

- Worked more on the create playlist endpoint. Andrew says we're really close! Sorting through Spotify's OAuth has been really challenging but also exciting to learn how to implement.
- There's a lot of back and forth going on between our app, the user, and the external API:

1. User gets to the spotify authorization page where they allow our app to access their Spotify information.
2. User gets redirected to our render page.
3. We receive a code as a response and use that to exchange for an access token.
4. The token will last for an hour and we'll use the token to create a new playlist in the user's account.

- Even though Andrew suggested using the OAuth2 library in requests, I was able to get some endpoints working with Spotipy! The code is a lot cleaner so I prefer it. It wasn't working before but after learning more about the OAuth workflow, I was able to make successful requests to create and update playlists. The missing piece was the auth url and receiving the code in response. Still need to figure out how to get the code programatically.
- I've spent a lot of time exploring OAuth but really think my time is going to be better spent on some of our other incomplete tasks. Now that I think about it, having the playlist generated through Spotify is just a small portion of our project scope. The main feature is still the swiping aspect. Still need to complete getting the songs displayed on the front end and then the frontend for all of the CRUD for playlists.

### November 29, 2022

- Worked with Tiffany to deploy our music microservice. It was very gratifying to see our site up on a URL that is not localhost!
- Considering other options if we aren't able to get the create playlist endpoint working with Spotify since we've been working on it for a week now. Rather than having a Spotify playlist at the end of the swiping feature, we may just show all of the liked songs as a list of embedded iFrame players instead.

### November 28, 2022

- Group programming with Andrew and James to get our post requests with Spotify working. We were dealing with the issue of the request hanging on SwaggerUI and thought that it could possibly be an issue of not using async await, however the use of it was never specified in the docs for Spotipy or Spotify API.
- We moved away from using Spotipy since it doesn't work well with FastAPI as they both want to handle redirects on their own. Playing around with making requests directly to Spotify API but running into a CORS and HTTPS issue. Andrew says we need to deploy our site first in order to make this work.

### November 25, 2022

- Group programming to look at the post request endpoints for Spotify. Wasn't making too much progress so we decided to shift gears and work on front end.
- Started on auth in the accounts microservice. Moved some things around, specifically the basemodels. I kept running into an issue where there was a circular import, so moved all the pydantic models from routers.users to db.py. Login/logout endpoints are showing up on Swagger UI.

### November 23, 2022

- Group programming to get the Get track recommendations endpoint working with FastAPI.
- Was able to figure out how to parse the JSON data so that it only returns the information that we want.
- The POST requests with Spotipy are proving to be a challenge as well. Running into an issue where we'd try to execute the the post request on Swagger UI but it just keeps loading until it times out. No error on the terminal either. The main difference between the get and post requests with Spotipy are that the post requests require user authentication.

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

We decided on having 3 total microservices. Since songs will all be incoming from a third party API (Spotify), I'm wondering if it's essential for it to have it's own database or if it can be shared with the playlists microservice.

### November 10, 2022

Today I worked on:

- Drafted endpoints for list playlist and update playlist
