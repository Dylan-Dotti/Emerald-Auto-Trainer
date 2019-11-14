import pyautogui as pag
import window_controller as wc


def locate_on_screen(img_url, quadrant=-1, confidence=0.99, num_attempts=1):
    for _ in range(num_attempts):
        if quadrant >= 0:
            region = wc.get_quadrant_rect(quadrant)
        else:
            region = wc.get_window_rect()
        res = pag.locateOnScreen(img_url, confidence=confidence, region=region)
        if res is not None:
            return res
    return None


def is_on_screen(img_url, quadrant=-1, confidence=0.99, num_attempts=1):
    return locate_on_screen(img_url, quadrant=quadrant, confidence=confidence, num_attempts=num_attempts) is not None
