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
    return round(x), round(y), round(width), round(height)


def get_row_rect(row):
    height = _square_height
    if row == 0 or row == num_rows() - 1:
        height /= 2.0
    y = row * _square_height
    if row != 0:
        y -= _square_height / 2.0
    x, y = wc.window_to_screen_coords((0, y))
    return round(x), round(y), round(wc.get_window_width()), round(height)


def get_col_rect(col):
    x, y = wc.window_to_screen_coords((col * _square_width, 0))
    return x, y, _square_width, wc.get_window_height()


def get_row_rects(row):
    return [get_rect_at(row, col)
            for col in range(num_cols())]


def get_col_rects(col):
    return [get_rect_at(row, col)
            for row in range(num_rows())]


def _get_params():
    _, _, width, height = wc.get_window_rect()
    square_width = width / float(num_cols())
    square_height = height / float(num_rows() - 1)
    return square_width, square_height


_square_width, _square_height = _get_params()
