import mouse_controller as mc
import time


def set_frame_skip(index):
    old_x, old_y = mc.get_mouse_position()
    click_options()
    mc.move_mouse_to(150, 25)
    time.sleep(.6)
    if index == 0:
        mc.click_at(370, 105)
    elif index == 1:
        mc.click_at(370, 140)
    else:
        raise Exception('Unsupported index')
    mc.move_mouse_to(old_x, old_y,
        is_global_coords=True)


def click_options():
    mc.click_at(90, -5)