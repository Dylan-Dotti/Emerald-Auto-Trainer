import window_grid as grid
import vision_agent as va
import window_controller as wc
import test_runtime as tr


def take_screenshot(row, col):
    file_url = 'img/ss_test/grid/grid_(%s_%s).png' % (row, col)
    print('Taking screenshot: ' + file_url)
    va.screenshot(file_url, region=grid.get_rect_at(row, col))


def take_row_screenshot(row):
    file_url = 'img/ss_test/grid/grid_row_%s.png' % row
    va.screenshot(file_url, region=grid.get_row_rect(row))


def take_col_screenshot(col):
    file_url = 'img/ss_test_grid/grid_col_%s.png' % col
    va.screenshot(file_url, region=grid.get_col_rect(col))


def test_grid_screenshots():
    for row in range(grid.num_rows()):
        for col in range(grid.num_cols()):
            file_url = 'img/ss_test/grid/grid_(%s_%s).png' % (row, col)
            va.screenshot(file_url, region=grid.get_rect_at(row, col))


def test_grid_row_screenshots(row):
    for col in range(grid.num_cols()):
        take_screenshot(row, col)


def test_grid_row_rect_screenshots():
    for row in range(grid.num_rows()):
        tr.get_avg_runtime(lambda: take_row_screenshot(row), 1)


def test_grid_col_rect_screenshots():
    for col in range(grid.num_cols()):
        take_col_screenshot(col)


if __name__ == '__main__':
    wc.set_window_foreground()
    print(tr.get_avg_runtime(lambda: test_grid_row_rect_screenshots(), 1))