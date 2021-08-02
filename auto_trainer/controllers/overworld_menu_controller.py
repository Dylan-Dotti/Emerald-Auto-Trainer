import time
import auto_trainer.controllers.keyboard_controller as kc
import auto_trainer.controllers.window_controller as wc
from auto_trainer.menu_controller import MenuController


_menu_on = False
_selector = MenuController(8)


def toggle_menu():
    set_menu_enabled(not _menu_on)
    kc.press_start()


def enable_menu():
    if not _menu_on:
        toggle_menu()


def disable_menu():
    if _menu_on:
        toggle_menu()


def set_menu_enabled(enabled):
    global _menu_on
    _menu_on = enabled


def select_pokemon_menu():
    _selector.move_to_index(1)
    kc.press_a()
    time.sleep(.8)


if __name__ == '__main__':
    wc.set_window_foreground_and_resize()
    select_pokemon_menu()
