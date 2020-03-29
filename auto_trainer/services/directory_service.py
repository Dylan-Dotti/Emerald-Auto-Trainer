import auto_trainer
import os


def get_auto_trainer_directory():
    return auto_trainer.__file__.replace('__init__.py', '')


def get_data_directory():
    return get_auto_trainer_directory() + 'data\\'