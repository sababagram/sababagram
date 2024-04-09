from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_ import Chat
from .reaction_type_ import ReactionType
from .user_ import User


@dataclass
class MessageReactionUpdated(BaseTelegramType):
    """
    This object represents a change of a reaction on a message performed by a user.

    Source: https://core.telegram.org/bots/api#messagereactionupdated
    """

    chat: Chat
    """
    The chat containing the message the user reacted to
    """
    message_id: int
    """
    Unique identifier of the message inside the chat
    """
    date: int
    """
    Date of the change in Unix time
    """
    old_reaction: list[ReactionType]
    """
    Previous list of reaction types that were set by the user
    """
    new_reaction: list[ReactionType]
    """
    New list of reaction types that have been set by the user
    """
    user: Optional[User] = None
    """
    *Optional*. The user that changed the reaction, if the user isn't anonymous
    """
    actor_chat: Optional[Chat] = None
    """
    *Optional*. The chat on behalf of which the reaction was changed, if the user is anonymous
    """
