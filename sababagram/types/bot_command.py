from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class BotCommand(BaseTelegramType):
    """
    This object represents a bot command.

    Source: https://core.telegram.org/bots/api#botcommand
    """

    command: str
    """
    Text of the command; 1-32 characters. Can contain only lowercase English letters, 
    digits and underscores.
    """
    description: str
    """
    Description of the command; 1-256 characters.
    """
