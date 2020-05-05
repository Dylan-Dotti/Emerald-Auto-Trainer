import auto_trainer.keyboard_controller as kc
import auto_trainer.window_controller as wc
import random


_menu_on = False
_menu_index = 0


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


def select_pokemon():
    _move_to_index(1)
    kc.press_a()


def _move_to_index(index):
    wc.set_window_foreground_and_resize()
    i_difference = abs(index - _menu_index)
    if i_difference < 4:
        key_func = (_move_cursor_up if index < _menu_index 
            else _move_cursor_down)
        for _ in range(i_difference):
            key_func()
    elif i_difference > 4:
        key_func = (_move_cursor_up if _menu_index < index
            else _move_cursor_down)
        for _ in range(8 - i_difference):
            key_func()
    else:
        key_func = random.choice([_move_cursor_up, _move_cursor_down])
        for _ in range(4):
            key_func()


def _move_cursor_up():
    global _menu_index
    _menu_index -= 1
    if _menu_index < 0:
        _menu_index = 7
    kc.press_up()


def _move_cursor_down():
    global _menu_index
    _menu_index = (_menu_index + 1) % 8
    kc.press_down()