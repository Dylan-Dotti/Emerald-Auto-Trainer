import win32gui as wgui
import pyautogui as pag
from battle_agent import BattleAgent
from services.path_data_service import get_path
from pokecenter_agent import PokeCenterAgent
import game_window_grid as gwg
import keyboard_controller as kc
import navigation.navigator as nav
import sys
import time
import time_controller as tc
import vision_agent as va
import window_controller as wc
import window_options_controller as woc


def move_and_check_battle(move_func):
    move_func()
    time.sleep(.1)
    return check_battle_start()


def check_battle_start():
    return va.is_in_window_quad('img/trainer_battle_sprite.png', 
        2, confidence=0.95)

def wait_for_battle_start(timeout=1.0):
    return va.wait_for_one_image('img/trainer_battle_sprite.png', 
        region=gwg.get_quadrant_rect(2), confidence=0.95, timeout=timeout)


def battle_loop(num_battles=1):
    print('battle loop')
    left = True
    for _ in range(num_battles):
        while not move_and_check_battle(
            kc.press_left if left else kc.press_right):
            left = not left
        left = not left
        BattleAgent().handle_battle()
        time.sleep(.75)


def train_loop(num_battles=1):
    woc.set_frame_skip(1)
    path = get_path('verdanturf town', 'route 111 left')
    nav.attempt_follow_path(path)
    tc.activate_speedup()
    if wait_for_battle_start():
        BattleAgent().handle_battle()
    kc.press_select()
    for _ in range(num_battles):
        kc.press_key_down('space')
        while not check_battle_start():
            pass
        kc.press_key_up('space')
        BattleAgent().handle_battle()
    tc.deactivate_speedup()
    kc.press_select()
    nav.attempt_follow_path(path, reversed=True)
    PokeCenterAgent().handle_pokecenter()


def follow_demo_path(reverse=False):
    path = get_path('mauville city', 'route 111 right')
    if reverse:
        path = reversed(
            [direct.get_opposite_direction() for direct in path])
    nav.attempt_follow_path(path, check_combat=True)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception('Expected at least one argument')
    wc.set_window_foreground_and_resize()
    time.sleep(.5)
    if sys.argv[1] == 'path_to':
        follow_demo_path()
    elif sys.argv[1] == 'path_from':
        follow_demo_path(reverse=True)
        PokeCenterAgent().handle_pokecenter()
    elif sys.argv[1] == 'battle_loop':
        if len(sys.argv) >= 3:
            battle_loop(int(sys.argv[2]))
        else:
            battle_loop()
    elif sys.argv[1] == 'train_loop':
        train_loop(num_battles=2)
    kc.alt_tab()
