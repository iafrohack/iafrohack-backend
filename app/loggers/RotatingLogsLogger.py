from interface import implements
import logging
from logging.handlers import TimedRotatingFileHandler
from typing import Dict
from .interfaces.LoggerInterface import LoggerInterface
from settings import LOGS_LOCATION_PATH
from containers.HelpersContainer import HelpersContainer
from .CoreLoggerWrapper import CoreLoggerWrapper

class RotatingLogsLogger(implements(LoggerInterface)):

    """
    The name of this logger
    """
    LOGGER_NAME = 'Rotating Log'

    """
    Logs will contain data worth this time-frame
    
    @see https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
    and https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/
    """
    ROTATION_DURATION = 'h'

    """
    How much time to wait before 
    creating a new log file
    
    @see https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
    and https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/
    """
    ROTATION_INTERVAL = 12

    """
    How many log files to store in addition to the 
    current log file. 
    
    @see https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
    and https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/
    """
    LOGS_BACKUP_COUNT = 60

    def __init__(self):
        self.logger = None

    def debug(self, message: str, context: Dict):
        """
        Log a debug level message
        :param message:
        :param context:
        :return:
        """
        logger = self.get_logger()
        logger.debug(message, extra=context)

    def error(self, message: str, context: Dict):
        """
        Log an error level message
        :param message:
        :param context:
        :return:
        """
        logger = self.get_logger()
        logger.error(message, extra=context)

    def info(self, message: str, context: Dict):
        """
        Log an info level message
        :param message:
        :param context:
        :return:
        """
        logger = self.get_logger()
        logger.info(message, extra=context)

    def warning(self, message: str, context: Dict):
        """
        Log a warning level message
        :param message:
        :param context:
        :return:
        """
        logger = self.get_logger()
        logger.warning(message, extra=context)

    def get_logger(self):
        """
        Instantiate and return the logger instance
        :return: logger instance
        """

        # TODO:: Implement async logging so that
        # logging does not affect performance as we scale

        if self.logger is not None:
            return self.logger

        logger = CoreLoggerWrapper(self.LOGGER_NAME)
        logger.setLevel(logging.DEBUG)

        # Setup configuration for the rotating logs storage
        handler = TimedRotatingFileHandler(LOGS_LOCATION_PATH,
                                       when=self.ROTATION_DURATION,
                                       interval=self.ROTATION_INTERVAL,
                                       backupCount=self.LOGS_BACKUP_COUNT)
        formatter = HelpersContainer.json_formatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger
        return self.logger

    def get_log_id(self) -> str:
        """
        Get a unique identifier of each log record
        :return:
        """
        return self.logger.get_log_id()

