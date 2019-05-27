from interface import Interface
from typing import Dict

class LoggerInterface(Interface):

    def debug(self, message: str, context: Dict):
        """
        Log a debug level message
        :param message:
        :param context:
        :return:
        """
        pass

    def error(self, message: str, context: Dict):
        """
        Log an error level message
        :param message:
        :param context:
        :return:
        """
        pass

    def info(self, message: str, context: Dict):
        """
        Log an info level message
        :param message:
        :param context:
        :return:
        """
        pass

    def warning(self, message: str, context: Dict):
        """
        Log a warning level message
        :param message:
        :param context:
        :return:
        """
        pass

    def get_log_id(self) -> str:
        """
        Get a unique identifier of each log record
        :return:
        """
        pass
