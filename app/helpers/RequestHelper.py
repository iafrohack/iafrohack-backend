from flask import request
import uuid

class RequestHelper(object):

    REQUEST_ID_HEADER = 'X-Request-Id'
    IDS_SEPARATOR_STRING = '_'

    def get_request_id(self, request: request) -> str:
        """
        Get a unique identifier of a request
        :param request:
        :return:
        """
        request_id = uuid.uuid4()
        request_x_id = request.headers.get(self.REQUEST_ID_HEADER)

        if request_x_id is None:
            return request_id

        return "{}{}{}".format(request_x_id, self.IDS_SEPARATOR_STRING, request_id)


