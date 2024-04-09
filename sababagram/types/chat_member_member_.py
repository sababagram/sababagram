from dataclasses import dataclass, field

from .chat_member_ import ChatMember
from .user_ import User


@dataclass
class ChatMemberMember(ChatMember):
    """
    Represents a `chat member <https://core.telegram.org/bots/api#chatmember>`_ that has no additional
    privileges or restrictions.

    Source: https://core.telegram.org/bots/api#chatmembermember
    """

    status: str = field(default="member", init=False)
    """
    The member's status in the chat, always “member”
    """
    user: User
    """
    Information about the user
    """
