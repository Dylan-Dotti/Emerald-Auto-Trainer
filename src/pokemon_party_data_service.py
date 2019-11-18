import json
import os
import pokemon


def load_party():
    f = open(_party_file_url)
    return json.loads(f.read())


def save_party(party_dict):
    f = open(_party_file_url, "w")
    f.write(json.dumps(party_dict, indent=2))


_party_file_url = 'data/party_pokemon.json'
