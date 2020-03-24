import auto_trainer.services.config_settings_data_service as csds
from auto_trainer.exceptions import WindowNotFoundError
import pyautogui as pag
import win32gui as wgui
import win32con as wcon
import time


def is_window_foreground():
    return wgui.GetForegroundWindow() == _get_window()


def wait_for_window_foreground(check_interval=1):
    while not is_window_foreground():
        time.sleep(check_interval)


def set_window_foreground():
    if is_window_minimized():
        wgui.ShowWindow(_get_window(), wcon.SW_RESTORE)
        time.sleep(.4)
    else:
        wgui.SetForegroundWindow(_get_window())
        time.sleep(.005)


def set_window_foreground_and_resize():
    resize_window_default()
    set_window_foreground()


def is_window_minimized():
    return wgui.IsIconic(_get_window()) == 1


def get_window_width():
    _, _, width, _ = get_window_rect()
    return width


def get_window_height():
    _, _, _, height = get_window_rect()
    return height


def resize_window(width, height):
    x, y, _, _ = get_window_rect()
    wgui.MoveWindow(_get_window(), x, y, width, height, True)


def resize_window_default():
    settings = csds.get_config_settings()
    resize_window(settings['default_win_height'],
        settings['default_win_width'])


def get_window_position_global():
    x, y, _, _ = get_window_rect()
    return x, y


def move_window(x, y):
    _, _, w, h = get_window_rect()
    wgui.MoveWindow(_get_window(), x, y, w, h, True)


def get_window_rect():
    mods = csds.get_win_border_mods('vba')
    rect = wgui.GetWindowRect(_get_window())
    x = rect[0] + mods['left']
    y = rect[1] + mods['top']
    width = rect[2] - x + mods['right']
    height = rect[3] - y + mods['bottom']
    return x, y, width, height


def get_window_center():
    x, y, width, height = get_window_rect()
    return round(x + width / 2), round(y + height / 2)


def global_to_local_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_window_rect()
    return x - window_x, y - window_y


def local_to_global_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_window_rect()
    return x + window_x, y + window_y


def _get_window():
    global __window
    if __window is None:
        __window = _find_window()
    return __window


def _find_window(speed_percent_limit=10000):
    for speed in range(speed_percent_limit):
        win_name = 'VisualBoyAdvance-'
        for s in [100, 10]:
            if speed < s:
                win_name += ' '
        win_name += str(speed) + '%'
        window = wgui.FindWindow(None, win_name)
        if window != 0:
            return window
    raise WindowNotFoundError('Could not find VBA window')


__window = None
