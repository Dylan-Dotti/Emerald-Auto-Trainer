# loads data from a json file and returns as a dictionary
# saves dictionary data to a json file
import json


_cache = {}


def load_data(file_url):
    if file_url not in _cache:
        f = open(file_url)
        data = json.loads(f.read())
        _cache[file_url] = data
        f.close()
    return _cache[file_url]


def save_data(file_url, data):
    f = open(file_url, 'w')
    data_json = json.dumps(data, indent=2)
    _cache[file_url] = data_json
    f.write(data_json)
    f.close()