import keyboard_controller as kc
import mouse_controller as mc
import time_controller as tc
import window_controller as wc
import window_options_controller as woc
import time
import sys


def get_num_rows():
    return 15


def get_num_cols():
    return 28


def fly_to_city(city_name):
    #woc.set_frame_skip(0)
    city_coords = _city_data[city_name]["coords"][0]
    corner_index = _get_closest_reachable_corner(city_coords)
    _move_to_corner(corner_index)
    _move_to_coords(
        _corner_coords[corner_index], city_coords)
    #woc.set_frame_skip(1)


def _move_to_coords(start_coords, end_coords):
    start_row, start_col = start_coords
    end_row, end_col = end_coords
    _move_to_col(start_col, end_col)
    _move_to_row(start_row, end_row)


def _move_to_row(start_row, end_row):
    row_dist = abs(end_row - start_row)
    if row_dist == 0:
        return
    if row_dist > 2 and row_dist % 2 != 0:
        if start_row < end_row:
            kc.press_down(duration=.1)
            start_row += 3
        else:
            kc.press_up(duration=.1)
            start_row -= 3
    time.sleep(.2)
    while start_row != end_row:
        if start_row < end_row:
            kc.press_down(duration=.05)
            start_row += 2
        else:
            kc.press_up(duration=.05)
            start_row -= 2
        time.sleep(.2)


def _move_to_col(start_col, end_col):
    col_dist = abs(end_col - start_col)
    if col_dist == 0:
        return
    while start_col != end_col:
        if start_col < end_col:
            kc.press_right()
            start_col += 2
        else:
            kc.press_left()
            start_col -= 2


def _move_to_corner(corner_index):
    tc.activate_speedup()
    if corner_index == 0:
        kc.press_left(duration=.15)
        kc.press_up(duration=.15)
    elif corner_index == 1:
        kc.press_right(duration=.15)
        kc.press_up(duration=.15)
    elif corner_index == 2:
        kc.press_left(duration=.15)
        kc.press_down(duration=.15)
    elif corner_index == 3:
        kc.press_right(duration=.15)
        kc.press_down(duration=.15)
    else:
        tc.deactivate_speedup()
        raise Exception('Unsupported index')
    tc.deactivate_speedup()


def _get_closest_reachable_corner(coords):
    corner_dists = _get_corner_dists(coords)
    reachable_corner_dists = {}
    for c_index, dist in corner_dists.items():
        c_coords = _corner_coords[c_index]
        if _is_reachable_from_coords(coords, c_coords):
            reachable_corner_dists[c_index] = dist
    return min(reachable_corner_dists,
        key=reachable_corner_dists.get)



def _is_reachable_from_coords(start_coords, end_coords):
    start_row, start_col = start_coords
    end_row, end_col = end_coords
    row_dist = abs(end_row - start_row)
    col_dist = abs(end_col - start_col)
    if row_dist == 1:
        return False
    return col_dist % 2 == 0


def _get_manhattan_dist(start_coords, end_coords):
    start_row, start_col = start_coords
    end_row, end_col = end_coords
    return (abs(end_row - start_row) + 
            abs(end_col - start_col))


def _get_corner_dists(start_coords):
    return { i: _get_manhattan_dist(
        start_coords, _corner_coords[i])
        for i in range(len(_corner_coords)) }


def _demo():
    for city in _city_data:
        fly_to_city(city)
        time.sleep(1)


_corner_coords = [
    (0, 0), (0, get_num_cols() - 1),
    (get_num_rows() - 1, 0), 
    (get_num_rows() - 1, get_num_cols() - 1)
]
_city_data = {
    "dewford town": {
        "coords": [(14, 2)],
        "img": "fly_locations/dewford.png"
    },
    "ever grande city - center": {
        "coords": [(9, 27)],
        "img": "fly_locations/center.png"
    },
    "ever grande city - league": {
        "coords": [(8, 27)],
        "img": "fly_locations/league.png"
    },
    "fallarbor town": {
        "coords": [(0, 3)],
        "img": "fly_locations/fallarbor.png"
    },
    "fortree city": {
        "coords": [(0, 12)],
        "img": "fly_locations/fortree.png"
    },
    "lavaridge town": {
        "coords": [(3, 5)],
        "img": "fly_locations/lavaridge.png"
    },
    "lilycove city": {
        "coords": [(3, 18), (3, 19)],
        "img": "fly_locations/lilycove.png"
    },
    "littleroot town": {
        "coords": [(11, 4)],
        "img": "fly_locations/littleroot.png"
    },
    "mauville city": {
        "coords": [(6, 8), (6, 9)],
        "img": "fly_locations/mauville.png"
    },
    "mossdeep city": {
        "coords": [(5, 24), (5, 25)],
        "img" : "fly_locations/mossdeep.png"
    },
    "oldale town": {
        "coords": [(9, 4)],
        "img": "fly_locations/oldale.png"
    },
    "pacifidlog town": {
        "coords": [(10, 17)],
        "img": "fly_locations/pacifidlog.png"
    },
    "petalburg city": {
        "coords": [(9, 1)],
        "img": "fly_locations/petalburg.png"
    },
    "rustboro city": {
        "coords": [(5, 0), (6, 0)],
        "img": "fly_locations/rustboro.png"
    },
    "slateport city": {
        "coords": [(10, 8), (11, 8)],
        "img": "fly_locations/slateport.png"
    },
    "sootopolis city": {
        "coords": [(7, 21)],
        "img": "fly_locations/sootopolis.png"
    },
    "verdanturf town": {
        "coords": [(6, 4)],
        "img": "fly_locations/verdanturf.png"
    }
}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception(
            'Expected 1 argument for destination')
    wc.set_window_foreground()
    if sys.argv[1] == 'demo':
        _demo()
    else:
        fly_to_city(sys.argv[1])