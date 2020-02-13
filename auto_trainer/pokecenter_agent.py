import vision_agent as va
import keyboard_controller as kc
import window_controller as wc
import time_controller as tc
import time

class PokeCenterAgent:
    def __init__(self):
        self._target_url = 'img/pokecenter_target.png'
        self._red_arrow_url = 'img/chat_red_arrow.png'
        self._blk_arrow_url = 'img/chat_black_arrow.png'
        self._wht_arrow_url = 'img/pokecenter_white_arrow.png'
        self._grn_arrow_url = 'img/pokecenter_green_arrow.png'
    
    def handle_pokecenter(self):
        tc.activate_speedup()
        while not va.is_in_window_half(self._target_url, 'top', confidence=0.65):
            kc.press_up()
        kc.press_a()
        for _ in range(2):
            self.wait_for_red_arrow()
            kc.press_a()
        self.wait_for_black_arrow()
        kc.press_a()
        self.wait_for_red_arrow()
        kc.press_a()
        time.sleep(.5)
        kc.press_a()
        tc.deactivate_speedup()
        while (not va.is_in_window_half(
            self._wht_arrow_url, 'bottom', 0.8) and
            not va.is_in_window_half(
            self._grn_arrow_url, 'bottom', 0.8)):
            kc.press_down()
        kc.press_down()
        time.sleep(1)
    
    def wait_for_red_arrow(self):
        if not va.wait_for_one_image(self._red_arrow_url, 
            region=wc.get_half_rect('bottom'), confidence=0.9):
            raise Exception('Failed to find red arrow')
    
    def wait_for_black_arrow(self):
        if not va.wait_for_one_image(self._blk_arrow_url, 
            region=wc.get_half_rect('right'), 
            confidence=0.9):
            raise Exception('Failed to find black arrow')


if __name__ == '__main__':
    wc.set_window_foreground_and_resize()
    #PokeCenterAgent().wait_for_red_arrow()
    PokeCenterAgent().handle_pokecenter()