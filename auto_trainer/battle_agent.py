import enum
import vision_agent as va
import keyboard_controller as kc
import pokemon_party as pparty
import pyautogui as pag
import time
import time_controller as tc
import game_window_grid as gwg


class BattleAgent:
    def __init__(self):
        self.__active_pokemon = pparty.get_active_pokemon()
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
        self.wait_for_black_arrow()
        moves = self.__active_pokemon.get_move_sequence(10)
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
                pparty.save_party()
                return
            else:
                # handle additional dialogues
                while not self.wait_for_black_arrow(timeout=0.1):
                    if self.wait_for_red_arrow(timeout=0.1):
                        print('additional dialogue detected')
                        kc.press_a()
        self.run_from_battle()

    def select_fight_option(self):
        if self.__menu_state == BAState.Main:
            self.move_cursor_to((0, 0))
            kc.press_a()
            self.__menu_state = BAState.Moves
        elif self.__menu_state != BAState.Moves:
            raise Exception('transition not implemented')

    def use_move(self, move_coords):
        print('Selecting move: ' + str(move_coords))
        self.select_fight_option()
        self.move_cursor_to(move_coords)
        kc.press_a()
        self.__menu_state = BAState.Main

    def use_move_and_check_faint(self, move_coords):
        self.use_move(move_coords)
        print('waiting for red or black arrow')
        self.wait_for_red_or_black_arrow()
        print('found arrow, checking enemy faint')
        return self.is_enemy_fainted()

    def run_from_battle(self):
        # need to account for failing to escape
        print('Attempting to run from battle')
        self.move_cursor_to((1, 1))
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()
        tc.deactivate_speedup()
        pparty.save_party()

    def is_enemy_fainted(self):
        return va.is_in_window_half('img/fainted.png', 'bottom', confidence=0.8)

    def on_enemy_fainted(self):
        print('Enemy fainted, concluding battle...')
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()

    def on_pokemon_leveled(self):
        print('pokemon leveled')
        self.__active_pokemon.increment_level()
        for _ in range(3):
            kc.press_a()

    def on_move_learned(self):
        print(self.__active_pokemon.get_name() + ' learned move')
        self.wait_for_red_arrow()
        kc.press_a()

    def on_move_attempt_learn(self):
        pass

    def wait_for_red_arrow(self, timeout=5.0):
        return va.wait_for_one_image(self._red_arrow_url, 
            confidence=.85, timeout=timeout,
            region=gwg.get_half_rect('bottom'))

    def wait_for_black_arrow(self, timeout=5.0):
        return va.wait_for_one_image(self._blk_arrow_url, 
            confidence=.85, timeout=timeout)

    def wait_for_red_or_black_arrow(self, timeout=5.0):
        return va.wait_for_one_image(self._red_arrow_url, 
            self._blk_arrow_url, confidence=.85, timeout=timeout,
            region=gwg.get_half_rect('bottom'))

    def wait_for_level_up(self):
        print('checking for level-up')
        return va.wait_for_one_image(self._leveled_url, confidence=.80,
            timeout=5.0)

    def wait_for_move_learned(self):
        print('checking for move learned')
        return va.wait_for_one_image(self._learned_url, confidence=.85,
            timeout=1.0)

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
            kc.press_down()
        elif curr_row > tar_row:
            kc.press_up()
        # left and right movement
        if curr_col < tar_col:
            kc.press_right()
        elif curr_col > tar_col:
            kc.press_left()


class BAState(enum.Enum):
    Main = 'Main'
    Moves = 'Moves'


if __name__ == '__main__':
    import window_controller as wc
    wc.set_window_foreground_and_resize()
    BattleAgent().handle_battle()
