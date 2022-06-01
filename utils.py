import os
import requests
from dotenv import load_dotenv

load_dotenv()

"""
Tokens stored in the .env file
"""
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
GEONAMES_KEY = os.getenv('GEONAMES_KEY')

__twitter_api__ = "https://api.twitter.com/2" # API url
__twitter_query__ = "/tweets/search/recent"   # API query (see documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction)

TWITTER_URL = f"{__twitter_api__}{__twitter_query__}"

"""
Functions
"""
def connect_to_endpoint(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
