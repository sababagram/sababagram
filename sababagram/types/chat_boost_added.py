from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ChatBoostAdded(BaseTelegramType):
    """
    This object represents a service message about a user boosting a chat.

    Source: https://core.telegram.org/bots/api#chatboostadded
    """

    boost_count: int
    """
    Number of boosts added by the user
    """
