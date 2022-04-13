import cachetools.func
import requests

@cachetools.func.ttl_cache(maxsize=128, ttl=3600)
def get_post_reddit(subreddit):
    try:
        params = (('limit', '10'),)
        response = requests.get('https://www.reddit.com/r/{}/top/.json'.format(subreddit), params=params)
        p = response.json()
        dadjokes = [value['data']['title'] + '\n' + value['data']['selftext']
         for value in p['data']['children']]
        return dadjokes
    except KeyError:
        return get_post_reddit(subreddit)