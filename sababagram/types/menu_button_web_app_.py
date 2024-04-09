from dataclasses import dataclass

from .base import BaseTelegramType
from .web_app_info_ import WebAppInfo


@dataclass
class MenuButtonWebApp(BaseTelegramType):
    """
    Represents a menu button, which launches a `Web App <https://core.telegram.org/bots/webapps>`_.

    Source: https://core.telegram.org/bots/api#menubuttonwebapp
    """

    type: str
    """
    Type of the button, must be *web_app*
    """
    text: str
    """
    Text on the button
    """
    web_app: WebAppInfo
    """
    Description of the Web App that will be launched when the user presses the button. 
    The Web App will be able to send an arbitrary message on behalf of the user using the method 
    :func:`sababagram.methods.answer_web_app_query`.
    """
