import auto_trainer.window_controller as wc


def test_init_window():
    print(wc.get_window_rect())
    wc.set_window_foreground()


if __name__ == '__main__':
    test_init_window()