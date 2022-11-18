import requests
import spotipy
import spotipy.util as util

# get track recommendations endpoint
endpoint_url = "https://api.spotify.com/v1/recommendations?"

client_id = "b18a943447ff4219ab09d47ac036a7b3"
client_secret = "b5963b5fbb9847668143360cd471e8e8"

# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify()
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()

OAuth_token= "BQBpTyVNF-bAfHqqhTuQ11WHzEua11DlACWO-TZ8_LGYnnRm_cVKLSJc5mpZNX-Tt0nVHrZ2rChQ6m7hoSy3FXisTowMOlIY44JkQJzohX4-6W7yKp-mkDUZDC8EOn2zSn5JlK9T3qCS_TnW2z_9W6Tb6-2iNLmcOh8BETzJump-_MGZYi3aHz324PBk5MW7zpWOE7y2tY6fGNo"

# util.prompt_for_user_token(username,scope,client_id={client_id},client_secret={client_secret},redirect_uri='your-app-redirect-url')

# OUR FILTERS
limit=10
market="US"
seed_genres="country"
uris=[]
# query
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}'

response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {OAuth_token}"})

json_response=response.json()
print(json_response)
print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")