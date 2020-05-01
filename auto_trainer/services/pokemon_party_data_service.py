# loads/saves pokemon data from/to the party_pokemon data file
import os
import auto_trainer.pokemon
import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.pokemon_file_service as pfs


def load_party():
    name_id_pairs = get_name_id_pairs()
    party_pokemon = [pfs.load_pokemon_from_file(n, i) 
        for (n, i) in name_id_pairs]
    return party_pokemon


def save_party(party_dict):
    jds.save_data(_party_file_url, party_dict)


def get_name_id_pairs():
    return [tuple(p) for p in jds.load_data(_party_file_url)]


_party_file_url = '%sparty_pokemon.json' % ds.get_data_directory()
