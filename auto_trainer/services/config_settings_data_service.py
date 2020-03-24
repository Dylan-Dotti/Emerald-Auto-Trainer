import auto_trainer.directory_manager as dm
import auto_trainer.services.json_data_service as jds


def get_config_settings():
    return jds.load_data(_settings_directory)


def get_default_win_size():
    settings = get_config_settings()
    return settings['default_win_height'], settings['default_win_width']


def get_win_border_mods(win_type):
    settings = get_config_settings()
    for mods in settings['win_border_mods']:
        if mods == win_type:
            return settings['win_border_mods'][mods]
    raise ValueError('Invalid win type')


def set_win_border_mods(win_type, new_mods):
    settings = get_config_settings()
    for mods in settings['win_border_mods']:
        if mods == win_type:
            settings['win_border_mods'][win_type] = new_mods
            jds.save_data(_settings_directory, settings)
            return
    raise ValueError('Invalid win type')


_settings_directory = (dm.get_data_directory() + 
    'configuration_settings.json')