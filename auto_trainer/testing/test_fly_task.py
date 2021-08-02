from auto_trainer.tasks.fly_task import FlyTask

if __name__ == '__main__':
    import auto_trainer.window_controller as wc
    wc.set_window_foreground_and_resize()
    FlyTask('sootopolis-city').execute()
    FlyTask('rustboro-city').execute()
    FlyTask('dewford-town').execute()
    FlyTask('lilycove-city').execute()
    FlyTask('verdanturf-town').execute()
    FlyTask('oldale-town').execute()
