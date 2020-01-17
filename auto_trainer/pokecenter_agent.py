import vision_agent as va
import keyboard_controller as kc
import window_controller as wc
import time_controller as tc
import time

class PokeCenterAgent:
    def __init__(self):
        self._target_url = 'img/pokecenter_target.png'
        self._door_url = 'img/pokecenter_open_door.png'
        self._red_arrow_url = 'img/chat_red_arrow.png'
        self._blk_arrow_url = 'img/battle_black_arrow.png'
    
    def handle_pokecenter(self):
        tc.activate_speedup()
        while not va.is_in_window_half(self._target_url, 'top', confidence=0.95):
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
        kc.press_down()
        tc.deactivate_speedup()
        while not va.is_in_window(self._door_url, confidence=0.75):
            kc.press_down()
    
    def wait_for_red_arrow(self):
        if not va.wait_for_one_image(self._red_arrow_url, 
            region=wc.get_half_rect('bottom'), confidence=0.9):
            raise Exception('Failed to find red arrow')
    
    def wait_for_black_arrow(self):
        if not va.wait_for_one_image(self._blk_arrow_url, 
            region=wc.get_half_rect('right'), confidence=0.9):
            raise Exception('Failed to find black arrow')


if __name__ == '__main__':
    wc.set_window_foreground()
    PokeCenterAgent().handle_pokecenter()