import auto_trainer.window_controller as wc
import auto_trainer.services.config_settings_data_service as csds


def num_rows():
    return 11


def num_cols():
    return 15


def get_square_width():
    _, _, width, _ = get_game_window_rect()
    return width / float(num_cols())


def get_square_height():
    _, _, _, height = get_game_window_rect()
    return height / float(num_rows() - 1)


def get_game_window_width():
    _, _, w, _ = get_game_window_rect()
    return w


def get_game_window_height():
    _, _, _, h = get_game_window_rect()
    return h


def get_game_window_center():
    x, y, width, height = get_game_window_rect()
    return round(x + width / 2), round(y + height / 2)


def get_game_window_rect():
    mods = csds.get_win_border_mods('game')
    x, y, w, h = wc.get_window_rect()
    x += mods['left']
    y += mods['top']
    w += mods['right'] - mods['left']
    h += mods['bottom'] - mods['top']
    return x, y, w, h



def get_quadrant_rect(index):
    x, y, _, _ = get_game_window_rect()
    mid_x, mid_y = get_game_window_center()
    half_width, half_height = mid_x - x, mid_y - y
    if index == 0:
        return x, y, half_width, half_height
    if index == 1:
        return mid_x, y, half_width, half_height
    if index == 2:
        return x, mid_y, half_width, half_height
    if index == 3:
        return mid_x, mid_y, half_width, half_height
    else:
        raise Exception('invalid quadrant index')


def get_half_rect(half_name):
    x, y, width, height = get_game_window_rect()
    mid_x, mid_y = get_game_window_center()
    half_width, half_height = mid_x - x, mid_y - y
    if half_name == 'top':
        return x, y, width, half_height
    if half_name == 'bottom':
        return x, mid_y, width, half_height
    if half_name == 'left':
        return x, y, half_width, height
    if half_name == 'right':
        return mid_x, y, half_width, height
    else:
        raise Exception('invalid half name')


def get_center_rect(width_percentage, height_percentage):
    _, _, width, height = get_game_window_rect()
    center_x, center_y = get_game_window_center()
    half_percent_width = round(width * width_percentage / 2)
    half_percent_height = round(height * height_percentage / 2)
    return (center_x - half_percent_width, center_y - half_percent_height,
        half_percent_width * 2, half_percent_height * 2)


def coords_in_range(row, col):
    return (row >= 0 and row < num_rows()
            and col >= 0 and col < num_cols())


def get_rect_at(row, col):
    width = get_square_width()
    x = col * width
    _, y, _, height = get_row_rect(row)
    return int(x), int(y), int(width), int(height)


def get_row_rect(row):
    height = get_square_height()
    if row == 0 or row == num_rows() - 1:
        height /= 2.0
    y = row * height
    if row != 0:
        y -= height / 2.0
    x, y = local_to_global_coords((0, y))
    return int(x), int(y), int(get_game_window_width()), int(height)


def get_row_rects(row):
    return [get_rect_at(row, col)
            for col in range(num_cols())]


def get_row_range_rect(min_row_incl, max_row_excl):
    if min_row_incl > max_row_excl - 1:
        raise ValueError('min row can\'t be greater than max row')
    min_x, min_y, _, _ = get_row_rect(min_row_incl)
    _, max_y, width, height = get_row_rect(max_row_excl - 1)
    return min_x, min_y, width, (max_y + height - min_y)


def get_col_rect(col):
    x, y = local_to_global_coords((col * get_square_width(), 0))
    # may need to change x, y between round and int
    return (round(x), round(y), int(get_square_height()), 
            int(get_game_window_height()))


def get_col_rects(col):
    return [get_rect_at(row, col)
            for row in range(num_rows())]


def get_col_range_rect(min_col_incl, max_col_excl):
    if min_col_incl > max_col_excl - 1:
        raise ValueError('min col can\'t be greater than max col')
    min_x, min_y, _, _ = get_col_rect(min_col_incl)
    max_x, _, max_width, max_height = get_col_rect(max_col_excl - 1)
    return min_x, min_y, max_x + max_width - min_x, max_height


def global_to_local_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_game_window_rect()
    return x - window_x, y - window_y


def local_to_global_coords(coords):
    x, y = coords
    window_x, window_y, _, _ = get_game_window_rect()
    return x + window_x, y + window_y
