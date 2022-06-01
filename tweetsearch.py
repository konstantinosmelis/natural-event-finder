from datetime import datetime, timedelta
import json
import requests
import utils

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {utils.BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_data(events):
    start_time = datetime.now() - timedelta(days=1)
    start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    for e in events:
        query_params = {
            'tweet.fields': 'created_at,geo',
            'max_results': '100',
            'start_time': start_time,
        }
        file = open(f"{e[1:len(e)]}.json", 'w')
        query_params['query'] = f'{e} -is:retweet -is:reply -has:mentions lang:en'
        json_response = connect_to_endpoint(utils.TWITTER_URL, query_params)
        file.write(json.dumps(json_response, indent=4, sort_keys=True))
        file.close()
