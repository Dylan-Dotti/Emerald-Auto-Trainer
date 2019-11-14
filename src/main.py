import win32gui as wgui
import pyautogui as pag
import battle_agent as ba
import keyboard_controller as kc
import time
import vision_agent as va

kc.alt_tab()
time.sleep(.5)
ba.BattleAgent().handle_battle()
time.sleep(1.5)
kc.alt_tab()
