from dataclasses import dataclass

from . import Chat, ChatBoost
from .base import BaseTelegramType


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
