
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from app.services.BlogsService import BlogsService
from app.services.ApiResponseHandler import ApiResponseHandler

from .RepositoriesContainer import RepositoriesContainer

repositories_container = RepositoriesContainer()

class ServicesContainer(containers.DeclarativeContainer):
    """IoC container of Services."""

    blogs = providers.Factory(BlogsService,
                                 repositories_container.blogs()
                                 )

    api_response_handler = providers.Factory(ApiResponseHandler)
