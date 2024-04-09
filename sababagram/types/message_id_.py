from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MessageId(BaseTelegramType):
    """
    This object represents a unique message identifier.

    Source: https://core.telegram.org/bots/api#messageid
    """

    message_id: int
    """
    Unique message identifier
    """
