import json
import os
import pokemon


def load_party():
    f = open(_party_file_url)
    data = json.loads(f.read())
    f.close()
    return data


def save_party(party_dict):
    f = open(_party_file_url, 'w')
    f.write(json.dumps(party_dict, indent=2))
    f.close()


_party_file_url = 'data/party_pokemon.json'
