import vision_agent as va
import test_runtime as trt
import window_controller as wc


def test_window_screenshot():
    print('Testing window screenshot...')
    img_name = 'img/ss_test/window_ss_test.png'
    wc.set_window_foreground()
    va.screenshot(file_name=img_name)
    print('Screenshot stored in: ' + img_name)


def test_runtime_window_screenshot():
    print('Testing window screenshot runtime...')
    wc.set_window_foreground()
    runtime = trt.get_avg_runtime(lambda: va.screenshot())
    print('Avg runtime: ' + str(runtime))


if __name__ == '__main__':
    test_window_screenshot()
    test_runtime_window_screenshot()
