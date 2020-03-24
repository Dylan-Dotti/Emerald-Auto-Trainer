import auto_trainer.directory_manager as dm
import auto_trainer.services.json_data_service as jds


def get_controls_map():
    controls_direct = dm.get_data_directory() + 'controls.json'
    return jds.load_data(controls_direct)