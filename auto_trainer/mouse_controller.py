import pyautogui as pag
import time
import window_controller as wc


def get_mouse_position():
    return pag.position()


def move_mouse_to(x, y, is_global_coords=False):
    if not is_global_coords:
        x, y = wc.window_to_screen_coords((x, y))
    pag.moveTo(x, y)


def click_at(x, y, is_global_coords=False):
    move_mouse_to(x, y, is_global_coords)
    pag.click()