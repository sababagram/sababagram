from dataclasses import dataclass
from typing import Optional

from . import Chat, ChatInviteLink, User
from .base import BaseTelegramType


@dataclass
class ChatJoinRequest(BaseTelegramType):
    """
    Represents a join request sent to a chat.

    Source: https://core.telegram.org/bots/api#chatjoinrequest
    """

    chat: Chat
    """
    Chat to which the request was sent
    """
    from_user: User
    """
    User that sent the join request
    """
    user_chat_id: int
    """
    Identifier of a private chat with the user who sent the join request. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a 64-bit integer or double-precision float type are safe for storing this identifier. 
    The bot can use this identifier for 5 minutes to send messages until the join request is 
    processed, assuming no other administrator contacted the user.
    """
    date: int
    """
    Date the request was sent in Unix time
    """
    bio: Optional[str] = None
    """
    *Optional*. Bio of the user.
    """
    invite_link: Optional[ChatInviteLink] = None
    """
    *Optional*. Chat invite link that was used by the user to send the join request
    """
