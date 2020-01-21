# controls navigation and actions
# in the pokemon party menu screen
import pokemon_party as pparty
import keyboard_controller as kc
import window_controller as wc
import time


def switch_pokemon(index_1, index_2):
    wc.set_window_foreground()
    select_pokemon(index_1)
    kc.press_down()
    kc.press_a()
    move_cursor_to(index_2)
    kc.press_a()
    time.sleep(.5)


def move_cursor_to(target_index):
    if target_index > pparty.party_size():
        raise Exception(
            'index higher than party size')
    global __cursor_index
    if (target_index == 0 and 
        __cursor_index != pparty.party_size()):
        kc.press_left()
        __cursor_index = 0
    while __cursor_index < target_index:
        kc.press_down()
        __cursor_index += 1
        time.sleep(.1)
    while __cursor_index > target_index:
        kc.press_up()
        __cursor_index -= 1
        time.sleep(.1)


def select_pokemon(pokemon_index):
    move_cursor_to(pokemon_index)
    kc.press_a()


__cursor_index = 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        wc.set_window_foreground()
        move_cursor_to(int(sys.argv[1]))
    else:
        raise Exception('Expected 1 argument')
