import battle_agent as ba
from navigation.direction import Direction
from navigation.localizer import Localizer
import keyboard_controller as kc
import vision_agent as va
import time
import time_controller as tc


def attempt_follow_path(path, check_combat=False, reversed=False):
    if reversed:
        path = _get_reverse_path(path)
    print('Attempting to follow path...')
    for direct in path:
        if not attempt_move_in_direction(direct, check_combat=check_combat):
            print('Aborted path: unsuccessful move')
            return False
    print('Path successful')
    return True


def attempt_move_in_direction(direct, num_attempts=10, check_combat=False):
    print('Attempting to move ' + direct.value + '...')
    for _ in range(num_attempts):
        Localizer.prepare_for_move(direct)
        move_in_direction(direct)
        time.sleep(.225)
        if Localizer.has_moved_in_direction(direct):
            print('Move confirmed')
            return True
        else:
            print('Move failed. Retrying...')
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


def _get_reverse_path(path):
    return reversed(
        [direct.get_opposite_direction() for direct in path])


def check_battle_start():
    return va.is_in_window('img/black_screen_top.png', confidence=0.98)
