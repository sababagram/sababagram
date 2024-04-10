from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class BotShortDescription(BaseTelegramType):
    """
    This object represents the bot's short description.

    Source: https://core.telegram.org/bots/api#botshortdescription
    """

    short_description: str
    """
    The bot's short description
    """
