from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ReactionTypeCustomEmoji(BaseTelegramType):
    """
    The reaction is based on a custom emoji.

    Source: https://core.telegram.org/bots/api#reactiontypecustomemoji
    """

    type: str
    """
    Type of the reaction, always “custom_emoji”
    """
    custom_emoji_id: str
    """
    Custom emoji identifier
    """
