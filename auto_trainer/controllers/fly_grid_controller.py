import auto_trainer.controllers.keyboard_controller as kc
import auto_trainer.controllers.mouse_controller as mc
import auto_trainer.controllers.time_controller as tc
import auto_trainer.controllers.window_controller as wc
import auto_trainer.controllers.window_options_controller as woc
import auto_trainer.services.cities_data_service as cds
import time
import sys


def fly_to_city(city_name):
    _move_to_city(city_name)
    kc.press_a()
    tc.activate_speedup()
    time.sleep(.5)
    tc.deactivate_speedup()


def _get_num_rows():
    return 15


def _get_num_cols():
    return 28


def _move_to_city(city_name):
    woc.set_frame_skip(0)
    city_coords = _city_coords[city_name][0]
    corner_index = _get_closest_reachable_corner(city_coords)
    _move_to_corner(corner_index)
    _move_to_coords(_corner_coords[corner_index], city_coords)
    woc.set_frame_skip(1)


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
            kc.press_down()
            start_row += 2
        else:
            kc.press_up(duration=0.01)
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
    return {i: _get_manhattan_dist(
        start_coords, _corner_coords[i])
        for i in range(len(_corner_coords))}


def _demo():
    for city_name in _city_coords.keys():
        _move_to_city(city_name)
        time.sleep(1)


_corner_coords = [
    (0, 0), (0, _get_num_cols() - 1),
    (_get_num_rows() - 1, 0),
    (_get_num_rows() - 1, _get_num_cols() - 1)
]
_city_coords = {
    'dewford-town': [[14, 2]],
    'ever grande city - center': [[9, 27]],
    'ever grande city - league': [[8, 27]],
    'fallarbor-town': [[0, 3]],
    'fortree-city': [[0, 12]],
    'lavaridge-town': [[3, 5]],
    'lilycove-city': [[3, 18], [3, 19]],
    'littleroot-town': [[11, 4]],
    'mauville-city': [[6, 8], [6, 9]],
    'oldale-town': [[9, 4]],
    'pacifidlog-town': [[10, 17]],
    'petalburg-city': [[9, 1]],
    'rustboro-city': [[5, 0], [6, 0]],
    'slateport-city': [[10, 8], [11, 8]],
    'sootopolis-city': [[7, 21]],
    'verdanturf-town': [[6, 4]]
}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception(
            'Expected 1 argument for destination')
    wc.set_window_foreground_and_resize()
    if sys.argv[1] == 'demo':
        _demo()
    else:
        fly_to_city((sys.argv[1]))
