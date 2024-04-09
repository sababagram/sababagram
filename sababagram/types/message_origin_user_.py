from dataclasses import dataclass

from .base import BaseTelegramType
from .user_ import User


@dataclass
class MessageOriginUser(BaseTelegramType):
    """
    The message was originally sent by a known user.

    Source: https://core.telegram.org/bots/api#messageoriginuser
    """

    type: str
    """
    Type of the message origin, always “user”
    """
    date: int
    """
    Date the message was sent originally in Unix time
    """
    sender_user: User
    """
    User that sent the message originally
    """
