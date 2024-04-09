from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_ import Chat


@dataclass
class MessageOriginChannel(BaseTelegramType):
    """
    The message was originally sent to a channel chat.

    Source: https://core.telegram.org/bots/api#messageoriginchannel
    """

    type: str
    """
    Type of the message origin, always “channel”
    """
    date: int
    """
    Date the message was sent originally in Unix time
    """
    chat: Chat
    """
    Channel chat to which the message was originally sent
    """
    message_id: int
    """
    Unique message identifier inside the chat
    """
    author_signature: Optional[str] = None
    """
    *Optional*. Signature of the original post author
    """
