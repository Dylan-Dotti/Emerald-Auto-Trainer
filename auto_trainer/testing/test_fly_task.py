if __name__ == '__main__':
    from auto_trainer.tasks.fly_task import FlyTask
    import auto_trainer.controllers.window_controller as wc

    wc.set_window_foreground_and_resize()
    FlyTask('sootopolis-city').execute()
    FlyTask('rustboro-city').execute()
    FlyTask('dewford-town').execute()
    FlyTask('lilycove-city').execute()
    FlyTask('verdanturf-town').execute()
    FlyTask('oldale-town').execute()
