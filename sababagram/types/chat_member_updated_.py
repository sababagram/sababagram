from dataclasses import dataclass
from typing import Optional, Union

from .base import BaseTelegramType
from .chat_ import Chat
from .chat_invite_link_ import ChatInviteLink
from .chat_member_administrator_ import ChatMemberAdministrator
from .chat_member_banned_ import ChatMemberBanned
from .chat_member_left_ import ChatMemberLeft
from .chat_member_member_ import ChatMemberMember
from .chat_member_owner_ import ChatMemberOwner
from .chat_member_restricted_ import ChatMemberRestricted
from .user_ import User


@dataclass
class ChatMemberUpdated(BaseTelegramType):
    """
    This object represents changes in the status of a chat member.

    Source: https://core.telegram.org/bots/api#chatmemberupdated
    """

    chat: Chat
    """
    Chat the user belongs to
    """
    from_user: User
    """
    Performer of the action, which resulted in the change
    """
    date: int
    """
    Date the change was done in Unix time
    """
    old_chat_member: Union[
        ChatMemberOwner,
        ChatMemberAdministrator,
        ChatMemberMember,
        ChatMemberRestricted,
        ChatMemberLeft,
        ChatMemberBanned,
    ]
    """
    Previous information about the chat member
    """
    new_chat_member: Union[
        ChatMemberOwner,
        ChatMemberAdministrator,
        ChatMemberMember,
        ChatMemberRestricted,
        ChatMemberLeft,
        ChatMemberBanned,
    ]
    """
    New information about the chat member
    """
    invite_link: Optional[ChatInviteLink] = None
    """
    *Optional*. Chat invite link, which was used by the user to join the chat; 
    for joining by invite link events only.
    """
    via_chat_folder_invite_link: Optional[bool] = None
    """
    *Optional*. True, if the user joined the chat via a chat folder invite link
    """
