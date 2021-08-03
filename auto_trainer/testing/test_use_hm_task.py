

if __name__ == '__main__':
    import sys
    import auto_trainer.controllers.window_controller as wc
    from auto_trainer.tasks.use_hm_task import UseHmTask

    if len(sys.argv) != 2:
        raise ValueError('Expected 1 argument, got ' + (len(sys.argv) - 1))

    wc.set_window_foreground_and_resize()
    UseHmTask(sys.argv[1]).execute()
