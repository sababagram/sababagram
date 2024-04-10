from dataclasses import dataclass

from . import ChatBoost
from .base import BaseTelegramType


@dataclass
class UserChatBoosts(BaseTelegramType):
    """
    This object represents a list of boosts added to a chat by a user.

    Source: https://core.telegram.org/bots/api#userchatboosts
    """

    boosts: list[ChatBoost]
    """
    The list of boosts added to the chat by the user
    """
