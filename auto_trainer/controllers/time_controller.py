import auto_trainer.controllers.keyboard_controller as kc
import time


def activate_speedup():
    kc.press_key_down('r')


def deactivate_speedup():
    kc.press_key_up('r')


def set_speed_multiplier(multiplier):
    if multiplier < 1 or multiplier > 10:
        raise ValueError('Invalid speed multiplier')
    kc.press_key_sequence('shiftleft', str(multiplier - 1))


def wait_for_seconds(duration):
    time.sleep(duration)
