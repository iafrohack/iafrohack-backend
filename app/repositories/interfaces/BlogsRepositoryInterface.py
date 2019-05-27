from interface import Interface

class BlogsRepositoryInterface(Interface):

    def fetch_post_by_id(self, blog_id):
        pass

    def fetch_all_posts(self):
        pass
