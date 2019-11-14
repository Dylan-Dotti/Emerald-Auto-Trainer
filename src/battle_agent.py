import enum
import vision_agent as va
import keyboard_controller as kc
import pyautogui as pag
import time


class BattleAgent:
    def __init__(self):
        self.__main_index = (0, 0)
        self.__moves_index = (0, 0)
        self.__menu_state = BAState.Main

    def handle_battle(self):
        self._wait_for_red_arrow()
        kc.press_a()
        self._wait_for_black_arrow()
        self.print_health()
        self.run_from_battle()

    def move_cursor_to(self, target_coords):
        if self.__menu_state == BAState.Main:
            self._press_cursor_buttons(self.__main_index, target_coords)
            self.__main_index = target_coords
        elif self.__menu_state == BAState.Moves:
            self._press_cursor_buttons(self.__moves_index, target_coords)
            self.__moves_index = target_coords

    def run_from_battle(self):
        # need to account for failing to escape
        self.move_cursor_to((1, 1))
        kc.press_a()
        self._wait_for_red_arrow()
        kc.press_a()

    def _press_cursor_buttons(self, curr_coords, tar_coords):
        curr_row, curr_col = curr_coords
        tar_row, tar_col = tar_coords
        # up and down movement
        if curr_row < tar_row:
            kc.press_down()
        elif curr_row > tar_row:
            kc.press_up()
        # left and right movement
        if curr_col < tar_col:
            kc.press_right()
        elif curr_col > tar_col:
            kc.press_left()

    def _wait_for_red_arrow(self):
        while not self._red_arrow_exists():
            time.sleep(.1)

    def _wait_for_black_arrow(self):
        while not self._black_arrow_exists():
            time.sleep(.1)

    def _red_arrow_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_red_arrow.png', confidence=0.8, num_attempts=num_attempts)

    def _black_arrow_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_black_arrow.png', confidence=0.8, num_attempts=num_attempts)

    def _battle_start_stripes_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_start_stripes.png', confidence=0.35, num_attempts=num_attempts)

    def print_health(self):
        if va.is_on_screen('img/health_bars/health_30.png', quadrant=3, confidence=0.9):
            print('Health is about 30%')
        else:
            print('Health is some other amount')


class BAState(enum.Enum):
    Main = 'Main'
    Moves = 'Moves'
