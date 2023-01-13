# Jam Pack'd

Jam Pack'd - Jam packed full of tasty jams

Created by:

- Joyce Yu
- Scott (Marble) Nideffer
- Tiffany Ameral
- Zoybh Hussein

## Design

- [Accounts API Design](docs/accounts-api-design.md)
- [Music API Design](docs/playlist-api-design.md)
- [Integrations](docs/integrations.md)
- [Data Models](docs/data-models.md)
- [Site navigation and Usage](docs/Navigation_Usage.md)

## Functionality

- JamPack'd is a music discovery app that will create a playlist based on randomly generated music that you can like or dislike.
- You need an account to use this app.
- Navigate to the Get Songs page to begin making a playlist.
- Select a genre from the dropdown menu and a song player will appear on the same page.
- If you dislike a song, the song will not be added to the playlist.
- If you like the song, the song will be added to a playlist.
- You may change genres at any time, be sure to hit the Submit button after selecting a knew genre.
- Hit Done when you are finished exploring songs.
- Add a name for your new playlist and jot down any thoughts that you have while listening to these new jams!
- You will be navigated to your new playlist for you to jam out.
- Created playlists can be viewed on My Playlists page.

## Project Initialization

To Start Jamming to new Tunes Follow these steps:

Clone the repository down to your local machine from:
<https://gitlab.com/semi-serious-solutions/jam-packd>

```
CD into the new project directory
```

Create a .ENV file:

Sign in or create a Spotify developer account and input these parameters within the .env file filling in the needed codes.

```
CLIENT_ID = "Your id"
CLIENT_SECRET = "Your secret"
```

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
