import pyautogui as pag
import services.controls_data_service as cds
import time


def press_key(key_name, num_times=1, duration=0, interval=0):
    for _ in range(num_times):
        pag.keyDown(key_name)
        if duration > 0:
            time.sleep(duration)
        pag.keyUp(key_name)
        if interval > 0:
            time.sleep(interval)


def press_key_down(key_name):
    pag.keyDown(key_name)


def press_key_up(key_name):
    return pag.keyUp(key_name)


def press_left(num_times=1, duration=0, interval=0):
    press_key(_controls_map['left'], num_times=num_times, 
        duration=duration, interval=interval)


def press_right(num_times=1, duration=0, interval=0):
    press_key(_controls_map['right'], num_times=num_times, 
        duration=duration, interval=interval)


def press_up(num_times=1, duration=0, interval=0):
    press_key(_controls_map['up'], num_times=num_times, 
        duration=duration, interval=interval)


def press_down(num_times=1, duration=0, interval=0):
    press_key(_controls_map['down'], num_times=num_times,
        duration=duration, interval=interval)


def press_a(num_times=1, duration=0, interval=0):
    press_key(_controls_map['a'], num_times=num_times,
        duration=duration, interval=interval)


def press_b(num_times=1, duration=0, interval=0):
    press_key(_controls_map['b'], num_times=num_times,
        duration=duration, interval=interval)


def press_start(num_times=1, duration=0, interval=0):
    press_key(_controls_map['start'], num_times=num_times,
        duration=duration, interval=interval)


def press_select(num_times=1, duration=0, interval=0):
    press_key(_controls_map['select'], num_times=num_times,
        duration=duration, interval=interval)


def alt_tab():
    pag.hotkey('alt', 'tab')


_controls_map = cds.get_controls_map()