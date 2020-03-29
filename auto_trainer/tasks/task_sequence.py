from auto_trainer.tasks.task import Task


class TaskSequence(Task):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = self.__init_tasks()
    
    def __init_tasks(self):
        raise NotImplementedError
    
    def execute(self):
        for task in self.tasks:
            task.execute()