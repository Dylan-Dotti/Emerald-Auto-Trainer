import keyboard_controller as kc


def activate_speedup():
    kc.press_key_down('r')


def deactivate_speedup():
    kc.press_key_up('r')
