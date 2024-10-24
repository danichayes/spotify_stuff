import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify credentials
client_id = '6ecdcf8f5f764184beda3928ef909dc6'
client_secret = '02c73992886640e9bec926a5b4591640'
redirect_uri = 'http://localhost:8888/callback/'
scope = 'playlist-read-private playlist-read-collaborative'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# This will automatically open the browser, get the token and return it
# Fetch the current user's playlists
def get_all_user_playlists(sp):
    playlists = []
    results = sp.current_user_playlists()
    playlists.extend([playlist for playlist in results['items'] if playlist['tracks']['total'] > 5])


    # While there are more playlists to fetch
    while results['next']:
        results = sp.next(results)
        playlists.extend([playlist for playlist in results['items'] if playlist['tracks']['total'] > 5])

    
    return playlists

# Print each playlist's name and ID
all_playlists = get_all_user_playlists(sp)
for playlist in all_playlists:
    print(f"Playlist Name: {playlist['name']} - Playlist ID: {playlist['id']}")

def get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])

    # Handle pagination
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

def get_playlist_selection(playlists):
    
    while True:
        playlist_input = input("Enter the playlist name or playlist ID: ")

        # Search for the playlist by name (if the input is not an ID)
        for playlist in all_playlists:
            if playlist_input == playlist['name'] or playlist_input == playlist['id']:
                return playlist['id']
        print("The name or ID you provided does not match any of the user's playlists")

# Retrieve the tracks from the playlist
playlist_id = get_playlist_selection(all_playlists)
tracks = get_playlist_tracks(sp, playlist_id)

for track in tracks:
    print({track['track']['name']})