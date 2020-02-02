import mouse_controller as mc
import keyboard_controller as kc
import time


def set_frame_skip(index):
    kc.press_key_sequence(['shiftleft', str(index)])