
import json
from app.services.interfaces.BlogsServiceInterface import BlogsServiceInterface
from app.services.interfaces.ApiResponseHandlerInterface import ApiResponseHandlerInterface
from app.services.ApiResponseHandler import ApiResponseHandler
from flask import Response

class BlogsController(object):

    def __init__(self,
                 blogs_service: BlogsServiceInterface,
                 api_response_handler: ApiResponseHandlerInterface
                 ):
        """

        :type blogs_service: BlogsServiceInterface
        """
        self._blogs_service = blogs_service
        self._api_response_handler = api_response_handler

    def show_home(self):
        return self._api_response_handler.success(json.dumps([]))

    def show_blog_post(self, blog_id) -> Response :
        try:
            blog_post = self._blogs_service.get_blog_post(blog_id)
            return self._api_response_handler.success(json.dumps(blog_post))
        except Exception as e:
            # TODO:: return all messages as unknown in the response for now
            error_message = ApiResponseHandler.UNKNOWN_ERROR_MESSAGE
            return self._api_response_handler.bad_request(error_message, e)

    # TODO:: implement limit & offset for the blogs
    def list_all_blog_posts(self) -> Response:

        try:
            blog_posts = self._blogs_service.get_all_blog_posts()
            return self._api_response_handler.success(json.dumps(blog_posts))
        except Exception as e:
            # TODO:: return all messages as unknown in the response for now
            error_message = ApiResponseHandler.UNKNOWN_ERROR_MESSAGE
            return self._api_response_handler.bad_request(error_message, e)
