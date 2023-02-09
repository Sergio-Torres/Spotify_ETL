from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import requests
import pandas as pd


def extract_data(): 
    input_variables = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
     
    date = datetime.now() - timedelta(days=5)
    date_unix_timestamp = int(date.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=date_unix_timestamp), headers = input_variables)
    data = r.json()
    
    return data

extract_data()

