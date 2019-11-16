import vision_agent as va
import test_runtime as trt


def test_runtime_window_screenshot():
    print('Testing window screenshot runtime...')
    runtime = trt.get_avg_runtime(lambda: va.screenshot())
    print('Avg runtime: ' + str(runtime))


if __name__ == '__main__':
    test_runtime_window_screenshot()
