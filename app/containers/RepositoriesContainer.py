
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repositories.BlogsRepository import BlogsRepository

from .ConnectionsContainer import ConnectionsContainer

connections_container = ConnectionsContainer()

class RepositoriesContainer(containers.DeclarativeContainer):
    """IoC container of Repositories"""

    blogs = providers.Factory(BlogsRepository, connections_container.db())
