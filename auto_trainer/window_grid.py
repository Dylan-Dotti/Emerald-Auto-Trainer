import window_controller as wc
import statistics as stat


def num_rows():
    return 11


def num_cols():
    return 15


def coords_in_range(row, col):
    return (row >= 0 and row < num_rows()
            and col >= 0 and col < num_cols())


def get_rect_at(row, col):
    width = _square_width
    x = col * width
    _, y, _, height = get_row_rect(row)
    return int(x), int(y), int(width), int(height)


def get_row_rect(row):
    height = _square_height
    if row == 0 or row == num_rows() - 1:
        height /= 2.0
    y = row * _square_height
    if row != 0:
        y -= _square_height / 2.0
    x, y = wc.window_to_screen_coords((0, y))
    return int(x), int(y), int(wc.get_window_width()), int(height)


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
    x, y = wc.window_to_screen_coords((col * _square_width, 0))
    return int(x), int(y), int(_square_width), int(wc.get_window_height())


def get_col_rects(col):
    return [get_rect_at(row, col)
            for row in range(num_rows())]


def get_col_range_rect(min_col_incl, max_col_excl):
    if min_col_incl > max_col_excl - 1:
        raise ValueError('min col can\'t be greater than max col')
    min_x, min_y, _, _ = get_col_rect(min_col_incl)
    max_x, _, max_width, max_height = get_col_rect(max_col_excl - 1)
    return min_x, min_y, max_x + max_width - min_x, max_height


def _get_params():
    _, _, width, height = wc.get_window_rect()
    square_width = width / float(num_cols())
    square_height = height / float(num_rows() - 1)
    return square_width, square_height


_square_width, _square_height = _get_params()
