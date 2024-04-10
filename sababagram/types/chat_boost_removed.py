from dataclasses import dataclass

from . import Chat, ChatBoostSource
from .base import BaseTelegramType


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
