from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat
from .chat_boost_ import ChatBoost


@dataclass
class ChatBoostUpdated(BaseTelegramType):
    """
    This object represents a boost added to a chat or changed.

    Source: https://core.telegram.org/bots/api#chatboostupdated
    """

    chat: Chat
    """
    Chat which was boosted
    """
    boost: ChatBoost
    """
    Information about the chat boost
    """
