import mouse_controller as mc
import keyboard_controller as kc
import time


def set_frame_skip(index):
    if index < 0 or index > 9:
        raise ValueError('Invalid frame skip index')
    kc.press_key_sequence('shiftleft', str(index))