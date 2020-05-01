# loads/saves pokemon data from/to the party_pokemon data file
import os
import auto_trainer.pokemon
import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.pokemon_file_service as pfs


def load_party():
    name_id_pairs = jds.load_data(_party_file_url)
    party_pokemon = [pfs.load_pokemon_from_file(n, i) 
        for (n, i) in name_id_pairs]
    for p in party_pokemon:
        print(p.get_name())
    return party_pokemon


def save_party(party_dict):
    jds.save_data(_party_file_url, party_dict)


_party_file_url = '%sparty_pokemon.json' % ds.get_data_directory()
