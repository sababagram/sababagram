from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat
from .chat_boost_source_ import ChatBoostSource


@dataclass
class ChatBoostRemoved(BaseTelegramType):
    """
    This object represents a boost removed from a chat.

    Source: https://core.telegram.org/bots/api#chatboostremoved
    """

    chat: Chat
    """
    Chat which was boosted
    """
    boost_id: str
    """
    Unique identifier of the boost
    """
    remove_date: int
    """
    Point in time (Unix timestamp) when the boost was removed
    """
    source: ChatBoostSource
    """
    Source of the removed boost
    """
