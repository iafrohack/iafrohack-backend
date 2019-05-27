from . import routes
from containers.ControllersContainer import ControllersContainer

controllers_container = ControllersContainer()

@routes.route('/posts/<blog_post_id>', methods=['GET'])
def show_blog_post(blog_post_id):
    blogs_controller = controllers_container.blogs()
    return blogs_controller.show_blog_post(blog_post_id)

@routes.route('/posts/', methods=['GET'])
def list_all_blog_posts():
    blogs_controller = controllers_container.blogs()
    return blogs_controller.list_all_blog_posts()
