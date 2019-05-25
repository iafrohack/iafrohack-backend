
from interface import implements
from .interfaces.BlogsServiceInterface import BlogsServiceInterface
from repositories.interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface


class BlogsService(implements(BlogsServiceInterface)):

    def __init__(self,
                 blogs_repository: BlogsRepositoryInterface):
        """

        :type blogs_repository: BlogsRepositoryInterface
        """
        self._blogs_repository = blogs_repository

    def get_blog(self, blog_id):

        blog_details = self._blogs_repository.fetch_by_id(blog_id)
        return {
            'id': blog_details.id,
            'content': blog_details.content,
            'createdAt': blog_details.created_at.isoformat(' '),
            'lastUpdatedAt': blog_details.last_updated_at.isoformat(' ')
        }

