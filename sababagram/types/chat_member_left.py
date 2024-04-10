from dataclasses import dataclass, field

from . import ChatMember, User


@dataclass
class ChatMemberLeft(ChatMember):
    """
    Represents a `chat member <https://core.telegram.org/bots/api#chatmember>`_ that isn't currently a
    member of the chat, but may join it themselves.

    Source: https://core.telegram.org/bots/api#chatmemberleft
    """

    status: str = field(default="left", init=False)
    """
    The member's status in the chat, always “left”
    """
    user: User
    """
    Information about the user
    """
