import json
import math
import os
from datetime import datetime

import pytz
import requests

with open('config.json', 'r') as file:
    config = json.load(file)
    API_KEY = config['API_KEY']

API_URL = (
    'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
