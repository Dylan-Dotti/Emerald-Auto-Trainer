# loads data from a json file and returns as a dictionary
# saves dictionary data to a json file
import json


def load_data(file_url):
    f = open(file_url)
    data = json.loads(f.read())
    f.close()
    return data


def save_data(file_url, data):
    f = open(file_url, 'w')
    f.write(json.dumps(data, indent=2))
    f.close()