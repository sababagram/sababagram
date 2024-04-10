from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MenuButtonCommands(BaseTelegramType):
    """
    Represents a menu button, which opens the bot's list of commands.

    Source: https://core.telegram.org/bots/api#menubuttoncommands
    """

    type: str
    """
    Type of the button, must be *commands*
    """
