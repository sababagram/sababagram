from dataclasses import dataclass

from .base import BaseTelegramType
from .user_ import User


@dataclass
class ChatBoostSourceGiftCode(BaseTelegramType):
    """
    The boost was obtained by the creation of Telegram Premium gift codes to boost a chat.
    Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium
    subscription.

    Source: https://core.telegram.org/bots/api#chatboostsourcegiftcode
    """

    source: str
    """
    Source of the boost, always “gift_code”
    """
    user: User
    """
    User for which the gift code was created
    """
