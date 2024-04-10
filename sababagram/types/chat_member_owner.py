from dataclasses import dataclass, field
from typing import Optional

from . import ChatMember, User


@dataclass
class ChatMemberOwner(ChatMember):
    """
    Represents a `chat member <https://core.telegram.org/bots/api#chatmember>`_ that owns the chat and
    has all administrator privileges.

    Source: https://core.telegram.org/bots/api#chatmemberowner
    """

    status: str = field(default="creator", init=False)
    """
    The member's status in the chat, always “creator”
    """
    user: User
    """
    Information about the user
    """
    is_anonymous: bool
    """
    *True*, if the user's presence in the chat is hidden
    """
    custom_title: Optional[str] = None
    """
    *Optional*. Custom title for this user
    """
