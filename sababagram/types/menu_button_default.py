from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MenuButtonDefault(BaseTelegramType):
    """
    Describes that no specific value for the menu button was set.

    Source: https://core.telegram.org/bots/api#menubuttondefault
    """

    type: str
    """
    Type of the button, must be *default*
    """
