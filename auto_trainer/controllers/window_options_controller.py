import auto_trainer.controllers.mouse_controller as mc
import auto_trainer.controllers.keyboard_controller as kc


def set_frame_skip(index):
    if index < 0 or index > 9:
        raise ValueError('Invalid frame skip index')
    kc.press_key_sequence('shiftleft', str(index))
