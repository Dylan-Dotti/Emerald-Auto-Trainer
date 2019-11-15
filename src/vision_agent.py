import pyautogui as pag
import window_controller as wc


def screenshot(file_name=None, region=wc.get_window_rect()):
    return pag.screenshot(imageFilename=file_name, region=region)


def locate_in_image(needle, haystack, confidence=0.99):
    return pag.locate(needle, haystack, confidence=confidence, region=wc.get_window_rect())


def locate_on_screen(img_url, region=wc.get_window_rect(), confidence=0.99, num_attempts=1):
    for _ in range(num_attempts):
        res = pag.locateOnScreen(img_url, region=region, confidence=confidence)
        if res is not None:
            return res
    return None


def locate_on_screen_quad(img_url, quadrant, confidence=0.99, num_attempts=1):
    return locate_on_screen(img_url, region=wc.get_quadrant_rect(quadrant), confidence=confidence, num_attempts=num_attempts)


def locate_on_screen_half(img_url, half_name, confidence=0.99, num_attempts=1):
    return locate_on_screen(img_url, region=wc.get_hemisphere_rect(half_name), confidence=confidence, num_attempts=num_attempts)


def is_in_image(needle, haystack, confidence=0.99):
    return locate_in_image(needle, haystack, confidence=0.99) is not None


def is_on_screen(img_url, confidence=0.99, num_attempts=1):
    return locate_on_screen(img_url, confidence=confidence, num_attempts=num_attempts) is not None


def is_on_screen_quad(img_url, quadrant, confidence=0.99, num_attempts=1):
    return locate_on_screen_quad(img_url, quadrant, confidence=confidence, num_attempts=num_attempts)


def is_on_screen_half(img_url, half_name, confidence=0.99, num_attempts=1):
    return locate_on_screen_half(img_url, half_name=half_name, confidence=confidence, num_attempts=num_attempts)
