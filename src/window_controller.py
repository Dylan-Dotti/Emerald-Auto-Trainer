import pyautogui as pag
import win32gui as wgui


def set_window_foreground():
    wgui.SetForegroundWindow(__window)


def get_scale():
    _, _, width, height = get_window_rect()
    for key, value in __resolutions.items():
        if value == (width, height):
            return key
    return 0


def get_window_width():
    _, _, width, _ = get_window_rect()
    return width


def get_window_height():
    _, _, _, height = get_window_rect()
    return height


def get_resolution():
    return __resolutions[get_scale()]


def get_window_rect():
    rect = wgui.GetWindowRect(__window)
    x = rect[0] + 10
    y = rect[1] + 65
    width = rect[2] - x - 10
    height = rect[3] - y - 12
    return x, y, width, height


def get_quadrant_rect(index):
    x, y, width, height = get_window_rect()
    mid_x, mid_y = round(x + width / 2), round(y + height / 2)
    half_width, half_height = mid_x - x, mid_y - y
    if index == 0:
        return x, y, half_width, half_height
    if index == 1:
        return mid_x, y, half_width, half_height
    if index == 2:
        return x, mid_y, half_width, half_height
    if index == 3:
        return mid_x, mid_y, half_width, half_height
    else:
        raise Exception('invalid quadrant index')


def get_half_rect(half_name):
    x, y, width, height = get_window_rect()
    mid_x, mid_y = round(x + width / 2), round(y + height / 2)
    half_width, half_height = mid_x - x, mid_y - y
    if half_name == 'top':
        return x, y, width, half_height
    if half_name == 'bottom':
        return x, mid_y, width, half_height
    if half_name == 'left':
        return x, y, half_width, height
    if half_name == 'right':
        return mid_x, y, half_width, height
    else:
        raise Exception('invalid half name')


def screen_to_window_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_window_rect()
    return x - window_x, y - window_y


def window_to_screen_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_window_rect()
    return x + window_x, y + window_y


def _find_window(scale_limit=1500):
    for i in range(scale_limit):
        query = 'VisualBoyAdvance-'
        if i < 100:
            query += ' '
        if i < 10:
            query += ' '
        query += str(i) + '%'
        window = wgui.FindWindow(None, query)
        if window != 0:
            return window
    return None


__resolutions = {
    1: (320, 274),
    2: (620, 474),
    3: (920, 674),
    4: (1220, 874)
}
__window = _find_window()
