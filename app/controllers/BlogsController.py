
from services.interfaces.BlogsServiceInterface import BlogsServiceInterface
import json

class BlogsController(object):

    def __init__(self,
                 blogs_service: BlogsServiceInterface):
        """

        :type blogs_service: BlogsServiceInterface
        """
        self._blogs_service = blogs_service

    def show(self, blog_id):
        response = self._blogs_service.get_blog(blog_id)
        return json.dumps(response)
