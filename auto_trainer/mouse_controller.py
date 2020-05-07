import pyautogui as pag
import time
import auto_trainer.game_window_grid as gwg
import auto_trainer.window_controller as wc


def get_mouse_position():
    return pag.position()


def move_mouse_to(x, y, is_global_coords=False):
    if not wc.is_window_foreground():
        print('waiting for window to be foreground for mouse event')
        wc.wait_for_window_foreground()
    if not is_global_coords:
        x, y = gwg.local_to_global_coords((x, y))
    pag.moveTo(x, y)


def click_at(x, y, is_global_coords=False):
    move_mouse_to(x, y, is_global_coords)
    pag.click()