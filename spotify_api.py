import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify credentials
client_id = '6ecdcf8f5f764184beda3928ef909dc6'
client_secret = '02c73992886640e9bec926a5b4591640'
redirect_uri = 'http://localhost:8888/callback/'
# scope = 'playlist-read-private'
scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# This will automatically open the browser, get the token and return it
results = sp.current_user_saved_tracks()
import pdb
pdb.set_trace()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
