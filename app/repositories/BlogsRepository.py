from interface import implements
from .interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface
from models.BlogPost import BlogPost
from providers.connections.ConnectionsProviderInterface import ConnectionsProviderInterface


class BlogsRepository(implements(BlogsRepositoryInterface)):

    def __init__(self, connection_provider: ConnectionsProviderInterface):

        self.connection_provider = connection_provider

    def fetch_by_id(self, blog_id):
        """

        :param blog_id:
        :return:
        """
        connection_service = self.connection_provider.get_connection()
        blog_post = connection_service.query(BlogPost).filter(BlogPost.id == blog_id).first()
        return blog_post
