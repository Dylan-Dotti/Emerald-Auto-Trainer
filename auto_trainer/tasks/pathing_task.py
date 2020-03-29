import auto_trainer.navigation.navigator as nav
import auto_trainer.services.path_data_service as pds
from auto_trainer.tasks.task import Task


class PathingTask(Task):

    def __init__(self, source, destination):
        super().__init__()
        self._source = source
        self._destination = destination
        self._path = pds.get_path(source, destination)
    
    def execute(self):
        nav.attempt_follow_path(self._path)