import dependency_injector.containers as containers
import dependency_injector.providers as providers
from app.helpers.NumbersHelper import NumbersHelper
from app.helpers.JsonEncoderHelper import JsonEncoderHelper
from app.helpers.JsonFormatterHelper import JsonFormatterHelper
from app.helpers.RequestHelper import RequestHelper
from app.helpers.SessionHelper import SessionHelper

class HelpersContainer(containers.DeclarativeContainer):
    """IoC container of app.helpers."""

    numbers = providers.Factory(NumbersHelper)
    json_encoder = providers.Factory(JsonEncoderHelper)
    json_formatter = providers.Factory(JsonFormatterHelper)
    request_helper = providers.Factory(RequestHelper)
    session_helper = providers.Factory(SessionHelper)


