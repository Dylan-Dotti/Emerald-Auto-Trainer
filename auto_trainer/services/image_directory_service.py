import auto_trainer.services.directory_service as ds


def get_img_directory():
    return ds.get_auto_trainer_directory() + 'img\\'


def get_emerald_icon_direct():
    return get_img_directory() + 'gui\\emerald.ico'