
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from providers.connections.Postgres import Postgres as PostgresDbProvider

class ConnectionsContainer(containers.DeclarativeContainer):
    """IoC container of Database connections."""

    db = providers.Factory(PostgresDbProvider)
