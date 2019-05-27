
from interface import implements
from .interfaces.BlogsServiceInterface import BlogsServiceInterface
from repositories.interfaces.BlogsRepositoryInterface import BlogsRepositoryInterface
from typing import Dict, List

class BlogsService(implements(BlogsServiceInterface)):

    def __init__(self,
                 blogs_repository: BlogsRepositoryInterface):
        """

        :type blogs_repository: BlogsRepositoryInterface
        """
        self._blogs_repository = blogs_repository

    def get_blog_post(self, blog_id) -> Dict:

        blog_details = self._blogs_repository.fetch_post_by_id(blog_id)

        if not blog_details.id:
            return {}

        return {
            'id': blog_details.id,
            'content': blog_details.content,
            'createdAt': blog_details.created_at.isoformat(' '),
            'lastUpdatedAt': blog_details.last_updated_at.isoformat(' ')
        }

    def get_all_blog_posts(self) -> List:
        blog_posts = self._blogs_repository.fetch_all_posts()

        all_blog_posts = []

        for blog_details in blog_posts:
            all_blog_posts.append(
              {
                'id': blog_details.id,
                'content': blog_details.content,
                'createdAt': blog_details.created_at.isoformat(' '),
                'lastUpdatedAt': blog_details.last_updated_at.isoformat(' ')
             })

        return all_blog_posts
