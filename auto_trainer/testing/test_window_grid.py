import auto_trainer.game_window_grid as gwg
import auto_trainer.vision_agent as va
import auto_trainer.window_controller as wc
import auto_trainer.testing.test_runtime as tr
import auto_trainer.services.image_directory_service as ids


def take_grid_square_screenshot(row, col):
    file_url = ('%sss_test\\grid\\squares\\grid_(%s_%s).png' % 
        (_img_direct, row, col))
    print('Taking screenshot:', file_url)
    va.screenshot(file_url, region=gwg.get_rect_at(row, col))


def take_window_screenshot():
    file_url = '%sss_test\\grid\\game_window.png' % _img_direct
    print('Taking screenshot:', file_url)
    va.screenshot(file_url)


def take_row_screenshot(row):
    file_url = '%sss_test\\grid\\rows\\grid_row_%s.png' % (_img_direct, row)
    print('Taking screenshot:', file_url)
    va.screenshot(file_url, region=gwg.get_row_rect(row))


def take_col_screenshot(col):
    file_url = '%sss_test\\grid\\cols\\grid_col_%s.png' % (_img_direct, col)
    print('Taking screenshot:', file_url)
    va.screenshot(file_url, region=gwg.get_col_rect(col))


def take_quadrant_screenshot(quad_index):
    file_url = ('%sss_test\\grid\\quads\\grid_quad_%s.png' % 
        (_img_direct, quad_index))
    print('Taking screenshot:', file_url)
    va.screenshot(file_url, region=gwg.get_quadrant_rect(quad_index))


def take_half_screenshot(half_name):
    file_url = ('%sss_test\\grid\\halves\\grid_half_%s.png' % 
        (_img_direct, half_name))
    print('Taking screenshot:', file_url)
    va.screenshot(file_url, region=gwg.get_half_rect(half_name))


def test_grid_square_screenshots():
    for row in range(gwg.num_rows()):
        for col in range(gwg.num_cols()):
            file_url = ('%sss_test/grid/grid_(%s_%s).png' % 
                (_img_direct, row, col))
            va.screenshot(file_url, region=gwg.get_rect_at(row, col))


def test_grid_row_screenshots(row):
    for col in range(gwg.num_cols()):
        take_grid_square_screenshot(row, col)


def test_grid_row_rect_screenshots():
    for row in range(gwg.num_rows()):
        tr.get_avg_runtime(lambda: take_row_screenshot(row), 1)


def test_grid_col_rect_screenshots():
    for col in range(gwg.num_cols()):
        take_col_screenshot(col)


_img_direct = ids.get_img_directory()


if __name__ == '__main__':
    import sys
    wc.set_window_foreground()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'window':
            take_window_screenshot()
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'quad':
            take_quadrant_screenshot(int(sys.argv[2]))
        elif sys.argv[1] == 'half':
            take_half_screenshot(sys.argv[2])
    else:
        print('Total runtime:',
            tr.get_avg_runtime(lambda: test_grid_row_rect_screenshots(), 1))