import dependency_injector.containers as containers
import dependency_injector.providers as providers
from helpers.NumbersHelper import NumbersHelper
from helpers.JsonEncoderHelper import JsonEncoderHelper
from helpers.JsonFormatterHelper import JsonFormatterHelper
from helpers.RequestHelper import RequestHelper
from helpers.SessionHelper import SessionHelper

class HelpersContainer(containers.DeclarativeContainer):
    """IoC container of Helpers."""

    numbers = providers.Factory(NumbersHelper)
    json_encoder = providers.Factory(JsonEncoderHelper)
    json_formatter = providers.Factory(JsonFormatterHelper)
    request_helper = providers.Factory(RequestHelper)
    session_helper = providers.Factory(SessionHelper)


