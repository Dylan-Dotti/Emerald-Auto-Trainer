import win32gui as wgui


def find_window(scale_limit=500):
    for i in range(scale_limit):
        window = wgui.FindWindow(None, 'VisualBoyAdvance-' + str(i) + '%')
        if window != 0:
            return window
    return None


def set_window_foreground():
    wgui.SetForegroundWindow(__window)


def get_scale():
    _, _, width, height = get_window_rect()
    for key, value in __resolutions.items():
        if value == (width, height):
            return key
    return 0


def get_resolution(scale):
    return __resolutions[scale]


def get_window_rect():
    rect = wgui.GetWindowRect(__window)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y
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


def get_hemisphere_rect(hemi_name):
    x, y, width, height = get_window_rect()
    mid_x, mid_y = round(x + width / 2), round(y + height / 2)
    half_width, half_height = mid_x - x, mid_y - y
    if hemi_name == 'top':
        return x, y, width, half_height
    if hemi_name == 'bottom':
        return x, mid_y, width, half_height
    if hemi_name == 'left':
        return x, y, half_width, height
    if hemi_name == 'right':
        return mid_x, y, half_width, height
    else:
        raise Exception('invalid hemisphere name')


__resolutions = {
    1: (320, 274),
    2: (620, 474),
    3: (920, 674),
    4: (1220, 874)
}
__window = find_window()
