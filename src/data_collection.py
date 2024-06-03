import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
#import requests
#from bs4 import BeautifulSoup

# Import configuration variables directly
#SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
#SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_CLIENT_ID = '12d55e3548f746d68c6ca5f048cd9cb5'
SPOTIPY_CLIENT_SECRET = '8b3afbc27dd740beb457e4e7a9a7f60f'

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


# def get_billboard_top_100(date):
#     url = f"https://www.billboard.com/charts/hot-100/{date}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     songs = []
#     for song in soup.find_all('li', class_='chart-list__element'):
#         title = song.find('span', class_='chart-element__information__song').text
#         artist = song.find('span', class_='chart-element__information__artist').text
#         songs.append((title, artist))
#     return songs

def main():
    # sp = get_spotify_client()
    # artist_name = 'Ed Sheeran'
    # track_ids = get_top_tracks(sp, artist_name)
    # tracks_data = [get_track_data(sp, track_id) for track_id in track_ids]
    # spotify_df = pd.DataFrame(tracks_data)

    # date = '2021-04-01'
    # top_100_songs = get_billboard_top_100(date)
    # billboard_df = pd.DataFrame(top_100_songs, columns=['title', 'artist'])

    # # Merge the Spotify and Billboard dataframes on the 'title' and 'artist' columns
    # merged_df = pd.merge(spotify_df, billboard_df, on=['title', 'artist'], how='outer')

    # # Save the merged dataframe to a CSV file
    # merged_df.to_csv('data/raw/song_data.csv', index=False)
    # print('Data collection complete!')

    sp = get_spotify_client()
    
    # Get the top tracks from Spotify's charts
    top_tracks = sp.playlist_tracks('37i9dQZEVXbMDoHDwVN2tF', limit=100)  # Spotify's Global Top 100 playlist

    # Extract track data
    tracks_data = []
    for track in top_tracks['items']:
        track_data = get_track_data(sp, track['track']['id'])
        tracks_data.append(track_data)

    # Create a dataframe from the track data
    df = pd.DataFrame(tracks_data)

    # Save the dataframe to a CSV file
    df.to_csv('data/raw/spotify_top_100.csv', index=False)
    print('Data collection complete!')

if __name__ == '__main__':
    main()
