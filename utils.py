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
