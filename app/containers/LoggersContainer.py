import dependency_injector.containers as containers
import dependency_injector.providers as providers
from loggers.RotatingLogsLogger import RotatingLogsLogger

class LoggersContainer(containers.DeclarativeContainer):
    """IoC container of Loggers."""

    logger = providers.Factory(RotatingLogsLogger)
