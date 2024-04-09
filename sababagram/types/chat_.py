from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .birthdate_ import Birthdate
from .business_intro_ import BusinessIntro
from .business_location_ import BusinessLocation
from .business_opening_hours_ import BusinessOpeningHours
from .chat_location_ import ChatLocation
from .chat_permissions_ import ChatPermissions
from .chat_photo_ import ChatPhoto
from .message_ import Message
from .reaction_type_ import ReactionType


@dataclass
class Chat(BaseTelegramType):
    """
    This object represents a chat.

    Source: https://core.telegram.org/bots/api#chat
    """

    id: int
    """
    Unique identifier for this chat. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """
    type: str
    """
    Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    """
    title: Optional[str] = None
    """
    *Optional*. Title, for supergroups, channels and group chats
    """
    username: Optional[str] = None
    """
    *Optional*. Username, for private chats, supergroups and channels if available
    """
    first_name: Optional[str] = None
    """
    *Optional*. First name of the other party in a private chat
    """
    last_name: Optional[str] = None
    """
    *Optional*. Last name of the other party in a private chat
    """
    is_forum: Optional[bool] = None
    """
    *Optional*. *True*, if the supergroup chat is a forum (has  enabled)
    """
    photo: Optional[ChatPhoto] = None
    """
    *Optional*. Chat photo. Returned only in :func:`sababagram.methods.get_chat`.
    """
    active_usernames: Optional[list[str]] = None
    """
    *Optional*. If non-empty, the list of all ; for private chats, supergroups and channels. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    birthdate: Optional[Birthdate] = None
    """
    *Optional*. For private chats, the date of birth of the user. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    business_intro: Optional[BusinessIntro] = None
    """
    *Optional*. For private chats with business accounts, the intro of the business. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    business_location: Optional[BusinessLocation] = None
    """
    *Optional*. For private chats with business accounts, the location of the business. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    business_opening_hours: Optional[BusinessOpeningHours] = None
    """
    *Optional*. For private chats with business accounts, the opening hours of the business. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    personal_chat: Optional["Chat"] = None
    """
    *Optional*. For private chats, the personal channel of the user. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    available_reactions: Optional[list[ReactionType]] = None
    """
    *Optional*. List of available reactions allowed in the chat. If omitted, 
    then all `emoji reactions <https://core.telegram.org/bots/api#reactiontypeemoji>`_ are allowed. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    accent_color_id: Optional[int] = None
    """
    *Optional*. Identifier of the accent color for the chat name and backgrounds of the chat photo, 
    reply header, and link preview. 
    See `accent colors <https://core.telegram.org/bots/api#accent-colors>`_ for more details. 
    Returned only in :func:`sababagram.methods.get_chat`. 
    Always returned in :func:`sababagram.methods.get_chat`.
    """
    background_custom_emoji_id: Optional[str] = None
    """
    *Optional*. 
    Custom emoji identifier of emoji chosen by the chat for the reply header and link preview 
    background. Returned only in :func:`sababagram.methods.get_chat`.
    """
    profile_accent_color_id: Optional[int] = None
    """
    *Optional*. Identifier of the accent color for the chat's profile background. 
    See `profile accent colors <https://core.telegram.org/bots/api#profile-accent-colors>`_ for more 
    details. Returned only in :func:`sababagram.methods.get_chat`.
    """
    profile_background_custom_emoji_id: Optional[str] = None
    """
    *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    emoji_status_custom_emoji_id: Optional[str] = None
    """
    *Optional*. 
    Custom emoji identifier of the emoji status of the chat or the other party in a private chat. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    emoji_status_expiration_date: Optional[int] = None
    """
    *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, 
    in Unix time, if any. Returned only in :func:`sababagram.methods.get_chat`.
    """
    bio: Optional[str] = None
    """
    *Optional*. Bio of the other party in a private chat. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_private_forwards: Optional[bool] = None
    """
    *Optional*. *True*, 
    if privacy settings of the other party in the private chat allows to use 
    :code:`tg://user?id=<user_id>` links only in chats with the user. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_restricted_voice_and_video_messages: Optional[bool] = None
    """
    *Optional*. *True*, 
    if the privacy settings of the other party restrict sending voice and video note messages in the 
    private chat. Returned only in :func:`sababagram.methods.get_chat`.
    """
    join_to_send_messages: Optional[bool] = None
    """
    *Optional*. *True*, if users need to join the supergroup before they can send messages. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    join_by_request: Optional[bool] = None
    """
    *Optional*. *True*, 
    if all users directly joining the supergroup need to be approved by supergroup administrators. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    description: Optional[str] = None
    """
    *Optional*. Description, for groups, supergroups and channel chats. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    invite_link: Optional[str] = None
    """
    *Optional*. Primary invite link, for groups, supergroups and channel chats. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    pinned_message: Optional[Message] = None
    """
    *Optional*. The most recent pinned message (by sending date). 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    permissions: Optional[ChatPermissions] = None
    """
    *Optional*. Default chat member permissions, for groups and supergroups. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    slow_mode_delay: Optional[int] = None
    """
    *Optional*. For supergroups, 
    the minimum allowed delay between consecutive messages sent by each unprivileged user; 
    in seconds. Returned only in :func:`sababagram.methods.get_chat`.
    """
    unrestrict_boost_count: Optional[int] = None
    """
    *Optional*. For supergroups, 
    the minimum number of boosts that a non-administrator user needs to add in order to ignore slow 
    mode and chat permissions. Returned only in :func:`sababagram.methods.get_chat`.
    """
    message_auto_delete_time: Optional[int] = None
    """
    *Optional*. The time after which all messages sent to the chat will be automatically deleted; 
    in seconds. Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_aggressive_anti_spam_enabled: Optional[bool] = None
    """
    *Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. 
    The field is only available to chat administrators. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_hidden_members: Optional[bool] = None
    """
    *Optional*. *True*, 
    if non-administrators can only get the list of bots and administrators in the chat. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_protected_content: Optional[bool] = None
    """
    *Optional*. *True*, if messages from the chat can't be forwarded to other chats. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    has_visible_history: Optional[bool] = None
    """
    *Optional*. *True*, if new chat members will have access to old messages; 
    available only to chat administrators. Returned only in :func:`sababagram.methods.get_chat`.
    """
    sticker_set_name: Optional[str] = None
    """
    *Optional*. For supergroups, name of group sticker set. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    can_set_sticker_set: Optional[bool] = None
    """
    *Optional*. *True*, if the bot can change the group sticker set. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    custom_emoji_sticker_set_name: Optional[str] = None
    """
    *Optional*. For supergroups, the name of the group's custom emoji sticker set. 
    Custom emoji from this set can be used by all users and bots in the group. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    linked_chat_id: Optional[int] = None
    """
    *Optional*. Unique identifier for the linked chat, i.e. 
    the discussion group identifier for a channel and vice versa; for supergroups and channel chats. 
    This identifier may be greater than 32 bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it is smaller than 52 bits, 
    so a signed 64 bit integer or double-precision float type are safe for storing this identifier. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
    location: Optional[ChatLocation] = None
    """
    *Optional*. For supergroups, the location to which the supergroup is connected. 
    Returned only in :func:`sababagram.methods.get_chat`.
    """
