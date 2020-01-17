import pyautogui as pag
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
    press_key('a', num_times=num_times, duration=duration, interval=interval)


def press_right(num_times=1, duration=0, interval=0):
    press_key('d', num_times=num_times, duration=duration, interval=interval)


def press_up(num_times=1, duration=0, interval=0):
    press_key('w', num_times=num_times, duration=duration, interval=interval)


def press_down(num_times=1, duration=0, interval=0):
    press_key('s', num_times=num_times, duration=duration, interval=interval)


def press_a(num_times=1, duration=0, interval=0):
    press_key('e', num_times=num_times, duration=duration, interval=interval)


def press_b(num_times=1, duration=0, interval=0):
    press_key('space', num_times=num_times,
              duration=duration, interval=interval)


def press_start(num_times=1, duration=0, interval=0):
    press_key('f', num_times=num_times,
              duration=duration, interval=interval)


def press_select(num_times=1, duration=0, interval=0):
    press_key('g', num_times=num_times,
              duration=duration, interval=interval)


def alt_tab():
    pag.hotkey('alt', 'tab')
