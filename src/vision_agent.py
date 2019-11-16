import pyautogui as pag
import window_controller as wc
import time


def screenshot(file_name=None, region=wc.get_window_rect()):
    return pag.screenshot(imageFilename=file_name, region=region)


def locate_in_image(needle, haystack, confidence=0.99):
    return pag.locate(needle, haystack, confidence=confidence, region=wc.get_window_rect())


def locate_in_region(img_url, region, confidence=0.99, num_attempts=1):
    for _ in range(num_attempts):
        res = pag.locateOnScreen(img_url, region=region, confidence=confidence)
        if res is not None:
            return res
    return None


def locate_in_window(img_url, confidence=0.99, num_attempts=1):
    return locate_in_region(img_url, region=wc.get_window_rect(), confidence=confidence, num_attempts=num_attempts)


def locate_in_window_quad(img_url, quadrant, confidence=0.99, num_attempts=1):
    return locate_in_region(img_url, wc.get_quadrant_rect(quadrant), confidence=confidence, num_attempts=num_attempts)


def locate_in_window_half(img_url, half_name, confidence=0.99, num_attempts=1):
    return locate_in_region(img_url, wc.get_half_rect(half_name), confidence=confidence, num_attempts=num_attempts)


def is_in_image(needle, haystack, confidence=0.99):
    return locate_in_image(needle, haystack, confidence=0.99) is not None


def is_in_region(img_url, region, confidence=0.99, num_attempts=1):
    return locate_in_region(img_url, region, confidence=confidence, num_attempts=1) is not None


def is_in_window(img_url, confidence=0.99, num_attempts=1):
    return locate_in_window(img_url, confidence=confidence, num_attempts=num_attempts) is not None


def is_in_window_quad(img_url, quadrant, confidence=0.99, num_attempts=1):
    return locate_in_window_quad(img_url, quadrant, confidence=confidence, num_attempts=num_attempts)


def is_in_window_half(img_url, half_name, confidence=0.99, num_attempts=1):
    return locate_in_window_half(img_url, half_name=half_name, confidence=confidence, num_attempts=num_attempts)


def wait_for_one_image(*img_urls, region=wc.get_window_rect(), confidence=0.99, timeout=1.0):
    start_time = time.time()
    elapsed = 0
    while elapsed < timeout:
        for img in img_urls:
            if is_in_region(img, region, confidence=confidence):
                return True
        elapsed = time.time() - start_time
    return False


def wait_for_all_images(*img_urls, region=wc.get_window_rect(), confidence=0.99, timeout=1.0):
    start_time = time.time()
    elapsed = 0
    while elapsed < timeout:
        all_found = True
        for img in img_urls:
            if not is_in_region(img, region, confidence=confidence):
                all_found = False
        if all_found:
            return True
        elapsed = time.time() - start_time
    return False
