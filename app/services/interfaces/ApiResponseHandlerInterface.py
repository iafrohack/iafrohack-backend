from interface import Interface
from flask import Response
import json

class ApiResponseHandlerInterface(Interface):

    def respond(self, data, status):
        pass

    def success(self, data: json) -> Response:
        """
        Success response
        :param data:
        :return:
        """
        pass

    def success_message(self, data: str) -> Response:
        """
        Bad Request response
        :param data:
        :return:
        """
        pass

    def bad_request(self, error_message: str, error: Exception) -> Response:
        """
        Bad Request response
        :param error:
        :return:
        """
        pass

    def internal_server_error(self, error: Exception) -> Response:
        """
        Internal Server error
        :param error:
        :return:
        """
        pass

    def error(self, error_message: str, error_code: int, error: Exception):
        """
        Handle logging and returning a response in case of errors
        :param error_message:
        :param error_code:
        :param error:
        :return:
        """
        pass
