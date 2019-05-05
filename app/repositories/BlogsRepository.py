from interface import implements
from .interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface


class BlogsRepository(implements(BlogsRepositoryInterface)):

    def fetch_by_id(self, blog_id):
        """

        :param blog_id:
        :return:
        """

        return "This is the blogId we will fetch data for: " + blog_id
