from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_ import Chat


@dataclass
class MessageOriginChat(BaseTelegramType):
    """
    The message was originally sent on behalf of a chat to a group chat.

    Source: https://core.telegram.org/bots/api#messageoriginchat
    """

    type: str
    """
    Type of the message origin, always “chat”
    """
    date: int
    """
    Date the message was sent originally in Unix time
    """
    sender_chat: Chat
    """
    Chat that sent the message originally
    """
    author_signature: Optional[str] = None
    """
    *Optional*. For messages originally sent by an anonymous chat administrator, 
    original message author signature
    """
