from interface import Interface


class BlogsServiceInterface(Interface):

    def get_blog_post(self, blog_id):
        pass

    def get_all_blog_posts(self):
        pass
