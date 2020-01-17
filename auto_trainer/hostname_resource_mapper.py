# maps computer hostname to the name of folders
# containing computer-specific data
import json_data_service as jds
import socket
import os


def get_folder_name():
    mappings = jds.load_data(__mapping_file_url)
    return mappings[socket.gethostname()]


def _add_mapping_from_input():
    mappings = jds.load_data(__mapping_file_url)
    hostname = socket.gethostname()
    print('Hostname:', hostname)
    folder_name = input('Enter a folder name to associate with this hostname: ')
    os.mkdir('img/' + folder_name)
    os.mkdir('data/' + folder_name)
    print('Folders created in img/ and data/')
    mappings[hostname] = folder_name
    jds.save_data(__mapping_file_url, mappings)
    print('Mapping successful')


__mapping_file_url = 'data/hostname_mapping.json'


if __name__ == '__main__':
    _add_mapping_from_input()