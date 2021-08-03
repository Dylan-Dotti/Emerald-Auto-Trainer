import random
import auto_trainer.controllers.keyboard_controller as kc
import auto_trainer.controllers.time_controller as tc


class MenuController:

    def __init__(self, menu_size, start_index=0):
        self._menu_size = menu_size
        self._start_index = start_index
        self._menu_index = start_index

    def move_to_index(self, index):
        tc.set_speed_multiplier(2)
        i_difference = abs(index - self._menu_index)
        half_size = self._menu_size / 2
        if i_difference < half_size or self._menu_size % 2 == 0:
            key_func = (self._move_cursor_up if index < self._menu_index
                        else self._move_cursor_down)
            for _ in range(i_difference):
                key_func()
        elif i_difference > half_size:
            key_func = (self._move_cursor_up if self._menu_index < index
                        else self._move_cursor_down)
            for _ in range(self._menu_size - i_difference):
                key_func()
        else:
            key_func = random.choice(
                [self._move_cursor_up, self._move_cursor_down])
            # change 4
            for _ in range(4):
                key_func()

    def select_index(self, index):
        self.move_to_index(index)
        kc.press_a()

    def _move_cursor_up(self):
        self._menu_index -= 1
        if self._menu_index < 0:
            self._menu_index = self._menu_size - 1
        kc.press_up()

    def _move_cursor_down(self):
        self._menu_index = (self._menu_index + 1) % self._menu_size
        kc.press_down()
