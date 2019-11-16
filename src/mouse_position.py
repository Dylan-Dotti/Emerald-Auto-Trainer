import pyautogui as pag
import window_controller as wc


if __name__ == '__main__':
    while True:
        print(wc.screen_to_window_coords(pag.position()), end='\r', flush=True)