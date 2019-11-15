import win32gui as wgui
import pyautogui as pag
import battle_agent as ba
import keyboard_controller as kc
import time
import vision_agent as va
import window_controller as wc


def move_and_check_battle(move_func):
    move_func()
    time.sleep(.1)
    return check_battle_start()


def check_battle_start(num_attempts=3):
    return va.is_on_screen('img/battle_start_stripes.png', confidence=0.35, num_attempts=num_attempts)


def battle_loop():
    left = True
    while True:
        while not move_and_check_battle((kc.press_left if left else kc.press_right)):
            left = not left
        left = not left
        ba.BattleAgent().handle_battle()
        time.sleep(1)


wc.set_window_foreground()
battle_loop()
kc.alt_tab()
