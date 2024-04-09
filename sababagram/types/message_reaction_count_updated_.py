from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat
from .reaction_count_ import ReactionCount


@dataclass
class MessageReactionCountUpdated(BaseTelegramType):
    """
    This object represents reaction changes on a message with anonymous reactions.

    Source: https://core.telegram.org/bots/api#messagereactioncountupdated
    """

    chat: Chat
    """
    The chat containing the message
    """
    message_id: int
    """
    Unique message identifier inside the chat
    """
    date: int
    """
    Date of the change in Unix time
    """
    reactions: list[ReactionCount]
    """
    List of reactions that are present on the message
    """
