
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repositories.BlogsRepository import BlogsRepository


class RepositoriesContainer(containers.DeclarativeContainer):
    """IoC container of Repositories"""

    blogs = providers.Factory(BlogsRepository)
