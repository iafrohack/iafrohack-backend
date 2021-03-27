from logging import Logger
import uuid
from app.loggers.CoreLogRecordWrapper import CoreLogRecordWrapper

class CoreLoggerWrapper(Logger):

    KEY_LOG_ID = 'log_id'

    NOTSET = 0

    def __init__(self, name: str, level=NOTSET):
        super().__init__(name, level)
        self.log_id = self.generate_log_id()

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info,
                   func=None, extra=None, sinfo=None):
        """
        In this method, we can add as much context as we
        want to the logs.

        @see https://stackoverflow.com/questions/12843099/python-logging-typeerror-not-all-arguments-converted-during-string-formatting/12843568?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
        :param name:
        :param level:
        :param fn:
        :param lno:
        :param msg:
        :param args:
        :param exc_info:
        :param func:
        :param extra:
        :param sinfo:
        :return:
        """
        rv = CoreLogRecordWrapper(name, level, fn, lno, msg, args, exc_info, func)
        if extra is not None:
            for key in extra:
                rv.__dict__[key] = extra[key]

        rv.__dict__[self.KEY_LOG_ID] = self.log_id
        return rv

    def get_log_id(self) -> str:
        """
        Get a unique identifier of each log record
        :return:
        """
        return self.log_id

    def generate_log_id(self) -> str:
        return str(uuid.uuid4())
