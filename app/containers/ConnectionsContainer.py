
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from providers.connections.FireStoreProvider import FireStoreProvider

class ConnectionsContainer(containers.DeclarativeContainer):
    """IoC container of Database connections."""

    db = providers.Factory(FireStoreProvider)
