import enum
import vision_agent as va
import keyboard_controller as kc
import pyautogui as pag
import time
import time_controller as tc


class BattleAgent:
    def __init__(self):
        self.__main_index = (0, 0)
        self.__moves_index = (0, 0)
        self.__menu_state = BAState.Main
        self._red_arrow_url = 'img/battle_red_arrow.png'
        self._blk_arrow_url = 'img/battle_black_arrow.png'
        self._fainted_url = 'img/fainted.png'
        self._leveled_url = 'img/grew.png'
        self._learned_url = 'img/learned.png'

    def handle_battle(self):
        print('Battle agent starting battle')
        tc.activate_speedup()
        self.wait_for_red_arrow()
        kc.press_a()
        print('Waiting for battle start...')
        self.wait_for_black_arrow()
        moves = [(0, 1), (0, 0), (0, 0), (0, 0), (0, 0)]
        for move in moves:
            # use move and check for enemy faint
            if self.use_move_and_check_faint(move):
                self.on_enemy_fainted()
                # check level up
                if self.wait_for_level_up():
                    self.on_pokemon_leveled()
                    # check move learned
                    if self.wait_for_move_learned():
                        self.on_move_learned()
                # check move attempt learn
                # check evolution
                tc.deactivate_speedup()
                return
        self.run_from_battle()

    def select_fight(self):
        if self.__menu_state == BAState.Main:
            self.move_cursor_to((0, 0))
            kc.press_a()
            self.__menu_state = BAState.Moves
        elif self.__menu_state != BAState.Moves:
            raise Exception('transition not implemented')

    def use_move(self, move_coords):
        print('Selecting move: ' + str(move_coords) + '...')
        self.select_fight()
        self.move_cursor_to(move_coords)
        kc.press_a()
        self.__menu_state = BAState.Main

    def use_move_and_check_faint(self, move_coords):
        self.use_move(move_coords)
        print('Waiting for move results...')
        va.wait_for_one_image(
            self._red_arrow_url, self._blk_arrow_url, confidence=0.95, timeout=10.0)
        return self.is_enemy_fainted()

    def run_from_battle(self):
        # need to account for failing to escape
        self.move_cursor_to((1, 1))
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()
        tc.deactivate_speedup()

    def is_enemy_fainted(self):
        return va.is_in_window_half('img/fainted.png', 'bottom', confidence=0.9)

    def on_enemy_fainted(self):
        print('Enemy fainted, concluding battle...')
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()

    def on_pokemon_leveled(self):
        for _ in range(3):
            kc.press_a()
        # handle move learning

    def on_move_learned(self):
        self.wait_for_red_arrow()
        kc.press_a()

    def on_move_attempt_learn(self):
        pass

    def wait_for_red_arrow(self, timeout=1.0):
        return va.wait_for_one_image(self._red_arrow_url, confidence=.95, timeout=timeout)

    def wait_for_black_arrow(self, timeout=1.0):
        return va.wait_for_one_image(self._blk_arrow_url, confidence=.95, timeout=timeout)

    def wait_for_red_or_black_arrow(self, timeout=1.0):
        return va.wait_for_one_image(self._red_arrow_url, self._blk_arrow_url, confidence=.95, timeout=timeout)

    def wait_for_level_up(self):
        return va.wait_for_one_image(self._leveled_url, confidence=.95)

    def wait_for_move_learned(self):
        return va.wait_for_one_image(self._learned_url, confidence=.95)

    def move_cursor_to(self, target_coords):
        if self.__menu_state == BAState.Main:
            self._press_cursor_buttons(self.__main_index, target_coords)
            self.__main_index = target_coords
        elif self.__menu_state == BAState.Moves:
            self._press_cursor_buttons(self.__moves_index, target_coords)
            self.__moves_index = target_coords

    def _press_cursor_buttons(self, curr_coords, tar_coords):
        curr_row, curr_col = curr_coords
        tar_row, tar_col = tar_coords
        # up and down movement
        if curr_row < tar_row:
            print('pressing down')
            kc.press_down()
        elif curr_row > tar_row:
            print('pressing up')
            kc.press_up()
        # left and right movement
        if curr_col < tar_col:
            print('pressing right')
            kc.press_right()
        elif curr_col > tar_col:
            print('pressing left')
            kc.press_left()

    # remove?
    def _battle_start_stripes_exists(self, num_attempts=1):
        return va.is_in_window('img/battle_start_stripes.png', confidence=0.35, num_attempts=num_attempts)


class BAState(enum.Enum):
    Main = 'Main'
    Moves = 'Moves'