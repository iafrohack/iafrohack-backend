
from services.interfaces.BlogsServiceInterface import BlogsServiceInterface

class BlogsController(object):

    def __init__(self,
                 blogs_service: BlogsServiceInterface):
        """

        :type blogs_service: BlogsServiceInterface
        """
        self._blogs_service = blogs_service

    def show(self, blog_id):
        return self._blogs_service.get_blog(blog_id)
