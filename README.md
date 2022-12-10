To Start Jamming to new Tunes Follow these steps:

Clone the repository down to your local machine from:
<https://gitlab.com/semi-serious-solutions/jam-packd>

CD into the new project directory

Create a .ENV file:

Sign in or create a Spotify dev account and input these parameters within the .env file filling in the needed codes.
CLIENT_ID = "Your id"
CLIENT_SECRET = "Your secret"

Create the Volumes in terminal:
Run volume create accounts
Run volume create music  

Starting up Docker in terminal:
Run docker compose build

Run docker compose up

Once you open your docker app:

Find ghi
Open in browser
  or
Navigate to :
<http://localhost:3000/>

Now you can make an account and start building your playlists.
