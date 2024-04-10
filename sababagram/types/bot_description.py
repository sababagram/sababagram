from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class BotDescription(BaseTelegramType):
    """
    This object represents the bot's description.

    Source: https://core.telegram.org/bots/api#botdescription
    """

    description: str
    """
    The bot's description
    """
