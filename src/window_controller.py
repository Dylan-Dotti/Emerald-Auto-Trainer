import win32gui as wgui

__window = None


def init_to_foreground_window():
    __window = wgui.GetForegroundWindow()

def get_window_rect():
    rect = wgui.GetWindowRect(__window)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y
    return x, y, width, height

