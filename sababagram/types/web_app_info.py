from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class WebAppInfo(BaseTelegramType):
    """
    Describes a `Web App <https://core.telegram.org/bots/webapps>`_.

    Source: https://core.telegram.org/bots/api#webappinfo
    """

    url: str
    """
    An HTTPS URL of a Web App to be opened with additional data as specified in `Initializing Web Apps 
    <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_
    """
