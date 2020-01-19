import services.json_data_service as jds


def get_controls_map():
    return jds.load_data('data/controls.json')