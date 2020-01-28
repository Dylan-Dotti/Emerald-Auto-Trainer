import requests


__cache = {}


def get_id(url, category):
    return url.replace(
        'https://pokeapi.co/api/v2/%s/' % 
        category, '').replace('/', '')


def get_urls(category):
    return [ res['url'] for res in get_results(category) ]


def get_results(category):
    url = 'https://pokeapi.co/api/v2/%s/?limit=10000' % category
    return _get_resource(url)['results']


def get_one(category, identifier):
    url = 'https://pokeapi.co/api/v2/%s/%s' % (category, identifier)
    return _get_resource(url)


def get_all(category):
    print('Fetching all %s...' % category)
    urls = get_urls(category)
    print('Fetching %s data...' % category)
    return _get_resources(urls)


def _get_resource(url):
    if url not in __cache:
        print('Fetching resource:', url)
        data = requests.get(url)
        __cache[url] = data.json()
    return __cache[url]


def _get_resources(urls):
    return [_get_resource(url) for url in urls]