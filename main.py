from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import requests
import pandas as pd


def extract(): 
    input_variables = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
     
    
    date = datetime.now() - timedelta(days=5)
    date_unix_timestamp = int(date.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=date_unix_timestamp), headers = input_variables)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    
    for song in data['items']:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
        
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }
    
    df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])

    return df

extract()

