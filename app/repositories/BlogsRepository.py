from interface import implements
from .interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface
from models.BlogPost import BlogPost
from providers.connections.ConnectionsProviderInterface import ConnectionsProviderInterface
from google.cloud import firestore

class BlogsRepository(implements(BlogsRepositoryInterface)):

    def __init__(self, connection_provider: ConnectionsProviderInterface):

        self.connection_provider = connection_provider

    def get_connection_provider(self):
        return self.connection_provider

    def fetch_post_by_id(self, blog_id):
        """

        :param blog_id:
        :return:
        """
        # select
        connection_service = self.connection_provider.get_connection
        blog_post = connection_service.collection(u"blogPosts").document(blog_id).get()
        return blog_post

    def fetch_all_posts(self):
        """

        :return:
        """
        connection_service = self.connection_provider.get_connection
        # select
        blog_posts = connection_service.collection(u"blogPosts").order_by(u'published_at', direction=firestore.Query.DESCENDING).stream()
        return blog_posts
