import auto_trainer.vision_agent as va
import auto_trainer.window_controller as wc
import auto_trainer.testing.test_runtime as trt


def test_window_screenshot():
    print('Testing window screenshot...')
    img_name = 'img/ss_test/window_ss_test.png'
    va.screenshot(file_name=img_name)
    print('Screenshot stored in: ' + img_name)


def test_half_screenshot(half_name):
    print('Testing window right half screenshot')
    img_name = 'img/ss_test/window_right_ss_test.png'
    va.screenshot(file_name=img_name, region=wc.get_half_rect(half_name))


def test_runtime_window_screenshot():
    print('Testing window screenshot runtime...')
    runtime = trt.get_avg_runtime(lambda: va.screenshot())
    print('Avg runtime: ' + str(runtime))


def test_detect_combat():
    print('Testing detect combat')
    img_name = 'img/battle_grass.png'
    while not va.is_in_window(img_name, confidence=0.95):
        print('False')
    print('True')


if __name__ == '__main__':
    wc.set_window_foreground()
    test_window_screenshot()
