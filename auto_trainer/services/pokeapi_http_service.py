import requests

__cache = {}

def _get_resource(url):
    if url not in __cache:
        data = requests.get(url)
        __cache[url] = data.json()
    return __cache[url]

def _get_resources(urls):
    return [_get_resource(url) for url in urls]

def get_urls(category):
    url = 'https://pokeapi.co/api/v2/%s/?limit=10000' % category
    if 'urls' not in __cache:
        print('Fetching urls for %s...' % category)
    else:
        print('Fetching urls for %s from cache...' % category)
    results = _get_resource(url)['results']
    return [ res['url'] for res in results ]

def get_one(category, identifier):
    url = 'https://pokeapi.co/api/v2/%s/%s' % (category, identifier)
    return _get_resource(url)

def get_all(category):
    print('Fetching all %s...' % category)
    urls = get_urls(category)
    print('Fetching %s data...' % category)
    return _get_resources(urls)