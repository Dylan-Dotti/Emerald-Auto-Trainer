import window_controller as wc
import statistics as stat


def _get_params():
    _, _, width, height = wc.get_window_rect()
    square_width = width / 15.0
    square_height = height / 10.0
    return square_width, square_height


_square_width, _square_height = _get_params()
print(_get_params())