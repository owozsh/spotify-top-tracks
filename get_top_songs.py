import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = input("Type your client_id: ")
client_secret = input("Type your client_secret: ")
redirect_uri= input("Type your redirect_uri: ")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-top-read"
))

topTracks = spotify.current_user_top_tracks()['items']

for track in topTracks:
    print(track['name'])
