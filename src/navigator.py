from direction import Direction
from localizer import Localizer
import keyboard_controller as kc
import vision_agent as va
import window_grid as grid
import time


def attempt_follow_path(path):
    print('Attempting to follow path...')
    for direct in path:
        if not attempt_move_in_direction(direct):
            print('Aborted path: unsuccessful move')
            return False
    print('Path successful')
    return True


def attempt_move_in_direction(direct, num_attempts=10):
    print('Attempting to move ' + direct.value)
    for _ in range(num_attempts):
        Localizer.prepare_for_move(direct)
        move_in_direction(direct)
        #time.sleep(.33)
        if Localizer.has_moved_in_direction(direct):
            print('Move confirmed')
            return True
        print('Move failed. Retrying...')
        #time.sleep(.1)
    print('Gave up after %s attempts' % str(num_attempts))
    return False


def move_in_direction(direct):
    if direct == Direction.up:
        kc.press_up()
    elif direct == Direction.down:
        kc.press_down()
    elif direct == Direction.left:
        kc.press_left()
    elif direct == Direction.right:
        kc.press_right()
    else:
        raise ValueError('Invalid direction')
