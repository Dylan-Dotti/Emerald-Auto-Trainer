import time
import auto_trainer.keyboard_controller as kc
import auto_trainer.window_controller as wc
from auto_trainer.menu_index_selector import MenuIndexSelector


_menu_on = False
_selector = MenuIndexSelector(8)


def toggle_menu():
    global _menu_on
    _menu_on = not _menu_on
    kc.press_start()


def enable_menu():
    if not _menu_on:
        toggle_menu()


def disable_menu():
    if _menu_on:
        toggle_menu()


def select_pokemon_menu():
    enable_menu()
    _selector.move_to_index(1)
    kc.press_a()
    time.sleep(.8)


if __name__ == '__main__':
    wc.set_window_foreground_and_resize()
    select_pokemon_menu()