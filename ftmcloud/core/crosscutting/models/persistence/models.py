import datetime
from enum import Enum


class TaskStatus(Enum):

    PENDING = "pending"
    FAILED = "failed"
    COMPLETED = "completed"


class TaskDocument:

    def __init__(
            self,
            pid: str,
            name: str,
            results: dict | None,
            status: TaskStatus,
            started_datetime: datetime.datetime,
            completed_datetime: datetime.datetime,
            task_executor: str
    ):
        self._pid = pid
        self._name = name
        self._results = results
        self._task_executor = task_executor
        self._status = status
        self._started_datetime = started_datetime
        self._completed_datetime = completed_datetime

    def __dict__(self):
        return {
            "pid": self._pid,
            "name": self._name,
            "status": str(self._status),
            "taskExecutor": self._task_executor,
            "startedDatetime": self._started_datetime,
            "completedDatetime": self._completed_datetime
        }
