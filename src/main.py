import win32gui as wgui
import pyautogui as pag
import battle_agent as ba
import keyboard_controller as kc
import navigator as nav
import sys
import time
import vision_agent as va
import window_controller as wc
from direction import Direction


def move_and_check_battle(move_func):
    move_func()
    time.sleep(.1)
    return check_battle_start()


def check_battle_start(num_attempts=3):
    return va.is_in_window('img/battle_start_stripes.png', confidence=0.35, )


def battle_loop(num_battles=1):
    left = True
    for _ in range(num_battles):
        while not move_and_check_battle((kc.press_left if left else kc.press_right)):
            left = not left
        left = not left
        ba.BattleAgent().handle_battle()
        time.sleep(.5)


def follow_demo_path():
    path = []
    path.extend([Direction.left for _ in range(4)])
    path.extend([Direction.up for _ in range(5)])
    path.extend([Direction.left for _ in range(28)])
    path.extend([Direction.up for _ in range(3)])
    path.append(Direction.left)
    nav.attempt_follow_path(path)


if len(sys.argv) == 1:
    raise Exception('Expected at least one argument')
wc.set_window_foreground()
time.sleep(.5)
if sys.argv[1] == 'path_to':
    follow_demo_path()
elif sys.argv[1] == 'battle_loop':
    if len(sys.argv) >= 3:
        battle_loop(int(sys.argv[2]))
    else:
        raise Exception('Expected argument for num battles')
kc.alt_tab()
