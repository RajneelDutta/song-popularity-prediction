import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os

# Import configuration variables directly
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

def get_spotify_client():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-library-read"
    ))
    return sp

def get_track_data(sp, track_id):
    track_info = sp.track(track_id)
    features = sp.audio_features(track_id)[0]
    track_data = {
        'name': track_info['name'],
        'artist': track_info['artists'][0]['name'],
        'album': track_info['album']['name'],
        'release_date': track_info['album']['release_date'],
        'popularity': track_info['popularity'],
        'danceability': features['danceability'],
        'energy': features['energy'],
        'key': features['key'],
        'loudness': features['loudness'],
        'mode': features['mode'],
        'speechiness': features['speechiness'],
        'acousticness': features['acousticness'],
        'instrumentalness': features['instrumentalness'],
        'liveness': features['liveness'],
        'valence': features['valence'],
        'tempo': features['tempo'],
    }
    return track_data

def get_top_tracks(sp, artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)
    track_ids = [track['id'] for track in top_tracks['tracks']]
    return track_ids

def main():
    sp = get_spotify_client()
    artist_name = 'Taylor Swift'
    track_ids = get_top_tracks(sp, artist_name)
    tracks_data = [get_track_data(sp, track_id) for track_id in track_ids]
    df = pd.DataFrame(tracks_data)
    df.to_csv('../data/raw/spotify_tracks.csv', index=False)
    print('Data collection complete!')

if __name__ == '__main__':
    main()