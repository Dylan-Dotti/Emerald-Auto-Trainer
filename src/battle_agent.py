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
        print('Battle agent starting battle')
        self.wait_for_red_arrow()
        kc.press_a()
        print('Waiting for battle start...')
        self.wait_for_black_arrow()
        moves = [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.wait_for_red_or_black_arrow()
        for move in moves:
            if self.use_move_and_check_faint(move):
                self.on_enemy_fainted()
                return
        self.run_from_battle()

    def move_cursor_to(self, target_coords):
        if self.__menu_state == BAState.Main:
            self._press_cursor_buttons(self.__main_index, target_coords)
            self.__main_index = target_coords
        elif self.__menu_state == BAState.Moves:
            self._press_cursor_buttons(self.__moves_index, target_coords)
            self.__moves_index = target_coords

    def select_fight(self):
        if self.__menu_state == BAState.Main:
            self.move_cursor_to((0, 0))
            kc.press_a()
            self.__menu_state = BAState.Moves
        elif self.__menu_state != BAState.Moves:
            raise Exception('transition not implemented')

    def use_move(self, move_coords):
        print('Selecting move...')
        self.select_fight()
        self.move_cursor_to(move_coords)
        kc.press_a()
        self.__menu_state = BAState.Main
    
    def use_move_and_check_faint(self, move_coords):
        self.use_move(move_coords)
        print('Waiting for move results...')
        self.wait_for_red_or_black_arrow()
        return self.is_enemy_fainted()

    def run_from_battle(self):
        # need to account for failing to escape
        self.move_cursor_to((1, 1))
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()
    
    def is_enemy_fainted(self):
        return va.is_on_screen_half('img/fainted.png', 'bottom', confidence=0.9)
    
    def on_enemy_fainted(self):
        print('Enemy fainted, concluding battle...')
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()
    
    def on_pokemon_leveled(self):
        kc.press_a()
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

    def wait_for_red_arrow(self):
        while not self._red_arrow_exists():
            time.sleep(.1)

    def wait_for_black_arrow(self):
        while not self._black_arrow_exists():
            time.sleep(.1)
    
    def wait_for_red_or_black_arrow(self):
        while not self._red_arrow_exists() and not self._black_arrow_exists():
            time.sleep(.1)

    def _red_arrow_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_red_arrow.png', confidence=0.8, num_attempts=num_attempts)

    def _black_arrow_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_black_arrow.png', confidence=0.8, num_attempts=num_attempts)

    def _battle_start_stripes_exists(self, num_attempts=1):
        return va.is_on_screen('img/battle_start_stripes.png', confidence=0.35, num_attempts=num_attempts)

    def print_health(self):
        check_percents = ['30', '50', '75', '80', '100']
        for percent in check_percents:
            if va.is_on_screen_half('img/health_bars/health_' + percent + '.png', 'bottom', confidence=0.975):
                print('Health is about ' + percent + '%')
                return
        print('Health is some other amount')


class BAState(enum.Enum):
    Main = 'Main'
    Moves = 'Moves'
