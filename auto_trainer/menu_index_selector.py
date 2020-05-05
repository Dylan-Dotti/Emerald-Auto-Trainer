import random
import auto_trainer.keyboard_controller as kc

class MenuIndexSelector:

    def __init__(self, menu_size, start_index=0):
        self._menu_size = menu_size
        self._start_index = start_index
        self._menu_index = start_index

    def _move_to_index(self, index):
        i_difference = abs(index - self._menu_index)
        half_size = self._menu_size / 2
        if i_difference < 4:
            key_func = (self._move_cursor_up if index < self._menu_index 
                else self._move_cursor_down)
            for _ in range(i_difference):
                key_func()
        elif i_difference > 4:
            key_func = (self._move_cursor_up if self._menu_index < index
                else self._move_cursor_down)
            for _ in range(8 - i_difference):
                key_func()
        else:
            key_func = random.choice(
                [self._move_cursor_up, self._move_cursor_down])
            for _ in range(4):
                key_func()

    def _move_cursor_up(self):
        self._menu_index -= 1
        if _menu_index < 0:
            _menu_index = 7
        kc.press_up()


    def _move_cursor_down(self):
        self._menu_index = (self._menu_index + 1) % 8
        kc.press_down()