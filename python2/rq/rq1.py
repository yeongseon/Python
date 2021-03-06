import requests

def count_words_at_url(url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())

from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

result = q.enqueue(count_words_at_url, 'http://nvie.com')