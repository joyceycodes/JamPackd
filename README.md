# Jam Pack'd

Jam Pack'd - Jam packed full of tasty jams

Created by:
- Joyce Yu
- Marble (Scott) Nideffer
- Tiffany Ameral
- Zoybh Hussein

## Design

- [Accounts Design](docs/accounts-api-design.md)
- [Playlist Design](docs/playlist-api-design.md)
- [Integrations](docs/integrations.md)
- [Data Models](docs/data-models.md)

## MVP
- JamPack'd is a music discovery app that will create a playlist based on randomly generated music that you can like or dislike.
- You need an account to use this app.
- If you dislike a song, the song will not be added to the playlist.
- If you like the song, the song will be added to a playlist for you that you can view after you're finished making your selections. 
- Created playlists can be viewed from Home Page-Logged In.

## Project Initialization

To Start Jamming to new Tunes Follow these steps:

Clone the repository down to your local machine from:
<https://gitlab.com/semi-serious-solutions/jam-packd>

```
CD into the new project directory
```

Create a .ENV file:

Sign in or create a Spotify dev account and input these parameters within the .env file filling in the needed codes.
CLIENT_ID = "Your id"
CLIENT_SECRET = "Your secret"


Create the Volumes in terminal:
```
docker volume create accounts
docker volume create music  
```

Starting up Docker in terminal:
```
docker compose build

docker compose up
```
Once you open your docker app:

Find ghi
Open in browser
  or
Navigate to :
<http://localhost:3000/>

Now you can make an account and start building your playlists.