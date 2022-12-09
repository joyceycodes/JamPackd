### December 8, 2022

- Finished the Update Playlist functionality with the help of some insight from James. Created a new Pydantic model that'll shape the data of the input for playlist update. It'll only take in data to change the name and comments for the playlist. In the future, I'd want to add functionality for the user to delete songs in a playlist and also allow users to add songs by navigating back to the Recommendations page.
- Worked with Z and Marble on the playlist list view page. We worked on the GET request to our database to get all the playlists.
- Updated Player.js so that it won't show the like and skip buttons if we've gone through the list of song recommendations. Once we've run out of songs, it'll only display the button that navigates them to the create playlist form.
- Implemented the functionality so that it only shows the playlists of a specific user once they're logged in.
  - At first, I thought the best approach would be by adding a user_id property in the PlaylistIn and PlaylistOut Pydantic models. This led me to have to update all the playlist endpoints with a user_id parameter as well. I wasn't sure how I was supposed to get that user_id but I wanted it to be the Mongo ID since it's a unique value associated with the user. We had created a get_user endpoint in our accounts microservice which returns the Mongo ID, but I needed to pass in the username in order to get there. Since the username is also technically supposed to be a unique ID as well, I opted to just use the username as the user_id so I wouldn't have to make one extra request to the accounts microservice. I tried lifting the setUsername state from login.js up to App.js, so that I'd be able to pass the username as props into all of the other endpoints that needed it. That worked with getting the username around. But then I was running into 422 unproccessable data issue because I was passing in the user_id as JSON, but in the Pydantic model, it requires a string input. Then my GET playlist endpoints needed to change into POST requests because I needed to pass in the user_id as a request body. This all became very complicated.
  - After consulting with other cohort mates, I was able to get more insight on how to approach this in a more efficient manner. Rather than getting the user_id in the front end, it's way easier to obtain in from the back end. In our queries, we are already passing in an account parameter that gets the current account data. Initially this was just used to verify that the user was signed in and to obtain the token, but within that data is also the user ID from Mongo! In our create playlist endpoint, we add a new key called user_id, and set the value equal to the Mongo ID, that way all the playlists created will have the user_id, and there's no need to make any changes to our front end code or our Pydantic models.

### December 7, 2022

- Spent most of the morning dealing with VS Code and Git issues. The Player.js file was causing me so much trouble. When I tried to commit all my changes, I kept running into an issue where the changes in that file would not want to be staged. I ended up deleting the whole file altogether since it was also in the remote branch of main. However, when I tried to pull from main, I noticed that I was able to pull all the changes except for that specific file. I ended up just recreating the file in my branch and the issues stopped there.
- My VSCode was also being strange and not showing merge conflicts properly. I had to update a user settings file in VSCode that was missing a comma, and that allowed me to configure the settings in VSCode to open the merge editor for files with conflicts as well as automatically navigate to the next file with a conflict. I'm not sure what caused my VSCode to behave this way but it started working properly after those fixes and a couple of updates to VSCode.
- Played around with the database connection for our deployed site. I was able to get data to show up in Mongo Atlas, which I believe will be for production, and in development, we'll be connected to MongoExpress.
- There was an accidental push to main that overrode some code functionality, worked with Z to get main back to how it was.
- Finished the playlist detail page. Added a navigate function that navigates to the detail page and set the query param to the playlist id. Used useParams for the first time to get information out of the current url.
  - It took a while to figure out why my map function wasn't working on this page. I spent a long time googling what I thought was the error message but it turns out I misunderstood the error in the console. I was running into a TypeError that could not read the value undefined for map(). Turns out the fix for this is to add a ternary before mapping to check if the list exists in the first place.
- Finished the Delete button for the playlist detail page.
- Realized we haven't added a way differentiate which playlists belong to which user. Will need to get that sorted tomorrow. As of right now, our get all playlist endpoint returns the playlists of all users. Most likely will need to include a user_id property to the playlist model.

### December 6, 2022

We're getting closer to finishing the MVP and it's so exciting to see our project come to life.

- Worked as a group to get our front end pages deployed. To be honest, they may have already been up. I had originally thought that the public url would be the render url, but it turns out it's the link with gitlab in it. Regardless, we add a new environment variable, REACT_APP_MUSIC, to both our gitlab.ci.yml and docker-compose.yml to build-front-end-job and ghi respectively. Still don't think our database is hooked up properly using the Mongo connection string but we'll have a lecture about it tomorrow.
- We were running into an error on render while deploying our music microservice that said it couldn't find a module for an import in our files. We were importing the authenticator functions from authenticator_music.py, and needed to add this in the deployment Dockerfile so that it gets copied during deployment.
- Worked with Tiffany on the Player component. Created a hook for the liked songs. It's initialized as an empty list and we're pushing to the list each time a user hits the Like button. Liked songs are saved in local storage after the user hits the DONE button. I learned that lists must be in JSON in order to save it in browser storage.
  - We were logging to the console each time the Liked songs list got updated with a new song and at first it seemed like the first Liked song was not being saved in state prooperly since the console was logging an empty array. It turns out that the useState hook runs async so the console log after it doesn't log the change. Thank you, StackOverflow.  
- Completed the Create Playlist form. It takes the liked songs from local storage and user input for the playlist name and additional comments about the playlist, then creates a POST request to our backend.
- Added front end auth to Create Playlist page and Recommendations/Player page.
- Removed id attribute from Song pydantic model since we don't need it. Am wondering if we want to keep ext_url in the Playlist models.

### December 5, 2022

- Worked on the 'Export to Spotify' button. Still unable to get it to work. I originally wanted to have the button navigate to the Spotify auth page, create a playlist, and then redirect back to our site. I'm having trouble with my function that gets the access token after the redirect and receive a 422 unprocessable entity error. After talking to Cam about it, it seems that my backend function to get the access token isn't working right either! I was under the assumption that I needed the code from the redirect uri to get the access token, but even without inputting in a valid code to my function, it still returns an access token. We tried to find where the token in being stored, but didn't find it anywhere in the session storage or cookies. It even worked in incognito mode in the browser which made things more interesting. I think the answer is somewhere within the Spotipy docs but since this has taken me so much time already, I think it's my time is best spent working on getting our MVP done. It is very likely being cached, because after clearing browser cahce, it requires reauthorization with Spotify.
- Worked on the player component on the front end. Tiffany already created a nice looking component with the Like and skip buttons. I'm passing the songs from the Recommendations component as props to the Player component. We need to show each song individually and move on to the next song once the user selects like or skip. Was able to get that working by creating a piece of State that updates onClick for the skip and like buttons. Need to save the liked songs in a list to be able to make a POST request on the next component.
- Noticed that there were failed GET requests for the token everytime we click on sign up or login page. It was showing that the endpoint was "/api/accounts/me/token" in the accounts router. Switched the authenticator function from get_current_account_data to try_get_current_account_data and it stopped the unnecessary GET requests. We use the try_get_current_account_data in any endpoints that you want the current account data, but it’s optional (from jwtdown-fastapi docs).

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
