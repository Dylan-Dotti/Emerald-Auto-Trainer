import auto_trainer.directory_manager as dm
import auto_trainer.services.pokeapi_http_service as phs
import requests
import os


def get_front_sprite_direct(pkm_name):
    pkm_name = pkm_name.lower()
    img_directory = dm.get_img_directory()
    file_direct = (img_directory + 
        'sprites\\%s_front_default.png' % pkm_name)
    # retrieve from file if exists
    if os.path.exists(file_direct):
        return file_direct
    # retreive from web
    pkm_data = phs.get_one('pokemon', pkm_name)
    sprite_url = pkm_data['sprites']['front_default']
    print('Fetching resource:', sprite_url)
    resp = requests.get(sprite_url, allow_redirects=True)
    open(file_direct, 'wb').write(resp.content)
    return file_direct