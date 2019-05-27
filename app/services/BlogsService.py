
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

        blog_post = self._blogs_repository.fetch_post_by_id(blog_id)

        if not blog_post.id:
            return {}

        blog_post_details = blog_post.content

        return {
                'id': blog_post.id,
                'title':  blog_post_details['title'],
                'summary': blog_post_details['summary'],
                'backgroundImage': blog_post_details['background_image'],
                'content': blog_post_details['content'],
                'createdAt': blog_post.created_at.isoformat(' '),
                'lastUpdatedAt': blog_post.last_updated_at.isoformat(' '),
                }


    def get_all_blog_posts(self) -> List:
        blog_posts = self._blogs_repository.fetch_all_posts()

        all_blog_posts = []

        for blog_details in blog_posts:

            blog_post_details = blog_details.content

            all_blog_posts.append(
              {
                'id': blog_details.id,
                'title':  blog_post_details['title'],
                'summary': blog_post_details['summary'],
                'backgroundImage': blog_post_details['background_image'],
                'createdAt': blog_details.created_at.isoformat(' '),
                'lastUpdatedAt': blog_details.last_updated_at.isoformat(' ')
             })

        return all_blog_posts
