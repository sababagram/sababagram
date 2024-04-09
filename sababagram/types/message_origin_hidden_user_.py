from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MessageOriginHiddenUser(BaseTelegramType):
    """
    The message was originally sent by an unknown user.

    Source: https://core.telegram.org/bots/api#messageoriginhiddenuser
    """

    type: str
    """
    Type of the message origin, always “hidden_user”
    """
    date: int
    """
    Date the message was sent originally in Unix time
    """
    sender_user_name: str
    """
    Name of the user that sent the message originally
    """
