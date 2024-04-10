from dataclasses import dataclass, field

from . import ChatMember, User


@dataclass
class ChatMemberBanned(ChatMember):
    """
    Represents a `chat member <https://core.telegram.org/bots/api#chatmember>`_ that was banned in the
    chat and can't return to the chat or view chat messages.

    Source: https://core.telegram.org/bots/api#chatmemberbanned
    """

    status: str = field(default="kicked", init=False)
    """
    The member's status in the chat, always “kicked”
    """
    user: User
    """
    Information about the user
    """
    until_date: int
    """
    Date when restrictions will be lifted for this user; Unix time. If 0, 
    then the user is banned forever
    """
