
from interface import implements
from .interfaces.ApiResponseHandlerInterface import ApiResponseHandlerInterface
from flask import Response, request, session
import json
from typing import Dict
from http import HTTPStatus
from containers.LoggersContainer import LoggersContainer
from containers.HelpersContainer import HelpersContainer
import traceback


class ApiResponseHandler(implements(ApiResponseHandlerInterface)):

    UNKNOWN_ERROR_MESSAGE = 'Something went wrong executing your request.' \
                            'Please try again later.'

    RESPONSE_KEY_SUCCESS = 'success'
    RESPONSE_KEY_MESSAGE = 'message'
    RESPONSE_KEY_DATA = 'data'
    RESPONSE_KEY_LOG_ID = 'log_id'

    def respond(self, data, status):
        """
        create a HTTP response
        :param data:
        :param status:
        :return:
        """
        return Response(
            data,
            status=status,
            mimetype='application/json'
        )

    def success(self, data: json) -> Response:
        """
        Success response
        :param data:
        :return:
        """
        return self.respond(data, HTTPStatus.OK)

    def success_message(self, data: str) -> Response:
        """
        Bad Request response
        :param data:
        :return:
        """
        response_data = {
            self.RESPONSE_KEY_DATA: data
        }
        return self.respond(json.dumps(response_data), HTTPStatus.OK)

    def bad_request(self, error_message: str, error: Exception) -> Response:
        """
        Bad Request response
        :param error:
        :return:
        """
        return self.error(error_message, HTTPStatus.BAD_REQUEST, error)

    def internal_server_error(self, error: Exception) -> Response:
        """
        Internal Server error
        :param error:
        :return:
        """
        return self.error(self.UNKNOWN_ERROR_MESSAGE, HTTPStatus.INTERNAL_SERVER_ERROR, error)

    def error(self, error_message: str, error_code: int, error: Exception):
        """
        Handle logging and returning a response in case of errors
        :param error_message:
        :param error_code:
        :param error:
        :return:
        """
        log_context = self.get_error_context(error_code)
        logger = LoggersContainer.logger()
        logger.error(str(error), log_context)

        response_data = {
            self.RESPONSE_KEY_MESSAGE: error_message,
            self.RESPONSE_KEY_LOG_ID: logger.get_log_id()
        }

        return self.respond(json.dumps(response_data), error_code)

    def get_error_context(self, error_code: int) -> Dict:
        """
        Get a request' context
        :return:
        """
        request_helper = HelpersContainer.request_helper()
        session_helper = HelpersContainer.session_helper()

        return {
            'ip': request.remote_addr,
            'session_id': session_helper.get_session_id(session),
            'request_id': request_helper.get_request_id(request),
            'http_method': request.method,
            'url': request.url,
            'code': error_code,
            'trace': traceback.format_exc(),
            'type': 'api_request'
        }
