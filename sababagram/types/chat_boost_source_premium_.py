from dataclasses import dataclass

from .base import BaseTelegramType
from .user_ import User


@dataclass
class ChatBoostSourcePremium(BaseTelegramType):
    """
    The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium
    subscription to another user.

    Source: https://core.telegram.org/bots/api#chatboostsourcepremium
    """

    source: str
    """
    Source of the boost, always “premium”
    """
    user: User
    """
    User that boosted the chat
    """
