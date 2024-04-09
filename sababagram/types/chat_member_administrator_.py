from dataclasses import dataclass, field
from typing import Optional

from .chat_member_ import ChatMember
from .user_ import User


@dataclass
class ChatMemberAdministrator(ChatMember):
    """
    Represents a `chat member <https://core.telegram.org/bots/api#chatmember>`_ that has some
    additional privileges.

    Source: https://core.telegram.org/bots/api#chatmemberadministrator
    """

    status: str = field(default="administrator", init=False)
    """
    The member's status in the chat, always “administrator”
    """
    user: User
    """
    Information about the user
    """
    can_be_edited: bool
    """
    *True*, if the bot is allowed to edit administrator privileges of that user
    """
    is_anonymous: bool
    """
    *True*, if the user's presence in the chat is hidden
    """
    can_manage_chat: bool
    """
    *True*, if the administrator can access the chat event log, get boost list, 
    see hidden supergroup and channel members, report spam messages and ignore slow mode. 
    Implied by any other administrator privilege.
    """
    can_delete_messages: bool
    """
    *True*, if the administrator can delete messages of other users
    """
    can_manage_video_chats: bool
    """
    *True*, if the administrator can manage video chats
    """
    can_restrict_members: bool
    """
    *True*, if the administrator can restrict, ban or unban chat members, 
    or access supergroup statistics
    """
    can_promote_members: bool
    """
    *True*, 
    if the administrator can add new administrators with a subset of their own privileges or demote 
    administrators that they have promoted, 
    directly or indirectly (promoted by administrators that were appointed by the user)
    """
    can_change_info: bool
    """
    *True*, if the user is allowed to change the chat title, photo and other settings
    """
    can_invite_users: bool
    """
    *True*, if the user is allowed to invite new users to the chat
    """
    can_post_stories: bool
    """
    *True*, if the administrator can post stories to the chat
    """
    can_edit_stories: bool
    """
    *True*, if the administrator can edit stories posted by other users
    """
    can_delete_stories: bool
    """
    *True*, if the administrator can delete stories posted by other users
    """
    can_post_messages: Optional[bool] = None
    """
    *Optional*. *True*, if the administrator can post messages in the channel, 
    or access channel statistics; for channels only
    """
    can_edit_messages: Optional[bool] = None
    """
    *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; 
    for channels only
    """
    can_pin_messages: Optional[bool] = None
    """
    *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only
    """
    can_manage_topics: Optional[bool] = None
    """
    *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; 
    for supergroups only
    """
    custom_title: Optional[str] = None
    """
    *Optional*. Custom title for this user
    """
