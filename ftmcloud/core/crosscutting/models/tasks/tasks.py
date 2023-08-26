from celery import Task


class BaseTask(Task):
    """
    Represents a base task that wraps the default Celery task.
    """

    def __init__(self):
        pass


class PipelineTask(Task):
    """
    Represents a sequence of tasks to be completed.
    """

    def __init__(self):
        pass


