from . import routes
from containers.ControllersContainer import ControllersContainer

controllers_container = ControllersContainer()

@routes.route('/blogs/<blog_id>', methods=['GET'])
def show_blog(blog_id):
    blogs_controller = controllers_container.blogs()
    return blogs_controller.show(blog_id)
