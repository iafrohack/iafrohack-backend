
from interface import implements
from .interfaces.BlogsServiceInterface import BlogsServiceInterface
from repositories.interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface


class BlogsService(implements(BlogsServiceInterface)):

    def __init__(self,
                 blogs_repository: BlogsRepositoryInterface):
        """

        :type blogs_repository: BlogsRepositoryInterface
        """
        self._propertyRepository = blogs_repository

    def get_blog(self, blog_id):
        return self._propertyRepository.fetch_by_id(blog_id)
