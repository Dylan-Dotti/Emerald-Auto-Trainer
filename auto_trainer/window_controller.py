import pyautogui as pag
import win32gui as wgui
import time


def is_window_foreground():
    return wgui.GetForegroundWindow() == __window


def wait_for_window_foreground(check_interval=1):
    while not is_window_foreground():
        time.sleep(check_interval)


def set_window_foreground():
    wgui.SetForegroundWindow(__window)
    time.sleep(.005)


def set_window_foreground_and_resize():
    resize_window_default()
    set_window_foreground()


def get_window_width():
    _, _, width, _ = get_window_rect()
    return width


def get_window_height():
    _, _, _, height = get_window_rect()
    return height


def resize_window(width, height):
    x, y, _, _ = get_window_rect()
    wgui.MoveWindow(__window, x, y, width, height, True)


def resize_window_default():
    resize_window(819, 600)


def get_window_position_global():
    x, y, _, _ = get_window_rect()
    return x, y


def move_window(x, y):
    _, _, w, h = get_window_rect()
    wgui.MoveWindow(__window, x, y, w, h, True)


def get_window_rect():
    rect = wgui.GetWindowRect(__window)
    x = rect[0] + 12
    y = rect[1] + 1
    width = rect[2] - x - 12
    height = rect[3] - y - 14
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
    return None


__window = _find_window()
