# loads/saves pokemon data from/to the party_pokemon data file
import services.json_data_service as jds
import os
import pokemon


def load_party():
    return jds.load_data(_party_file_url)


def save_party(party_dict):
    jds.save_data(_party_file_url, party_dict)


_party_file_url = 'data/party_pokemon.json'
