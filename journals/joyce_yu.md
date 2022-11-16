
### November 15, 2022
Today I worked on:
- Worked with the group on the Docker Compose file to get all the containers running for the playlists, songs, and accounts microservices.
- Started working on queries for playlists. Created playlists/db.py and playlists/models.py.

We decided on having 3 total microservices. Since songs will all be incoming from a third party API (Spotify), I'm wondering if it's essential for it do have it's own database or if it can be shared with the playlists microservice.

### November 10, 2022
Today I worked on:
- Drafted endpoints for list playlist and update playlist