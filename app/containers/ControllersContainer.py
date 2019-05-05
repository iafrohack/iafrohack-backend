
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from .ServicesContainer import ServicesContainer
from controllers.BlogsController import BlogsController

services_container = ServicesContainer()


class ControllersContainer(containers.DeclarativeContainer):
    """IoC container of Controllers """

    blogs = providers.Factory(BlogsController,
                                 services_container.blogs())
