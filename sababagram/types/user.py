from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class User(BaseTelegramType):
    """
    This object represents a Telegram user or bot.

    Source: https://core.telegram.org/bots/api#user
    """

    id: int
    """
    Unique identifier for this user or bot. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a 64-bit integer or double-precision float type are safe for storing this identifier.
    """
    is_bot: bool
    """
    *True*, if this user is a bot
    """
    first_name: str
    """
    User's or bot's first name
    """
    last_name: Optional[str] = None
    """
    *Optional*. User's or bot's last name
    """
    username: Optional[str] = None
    """
    *Optional*. User's or bot's username
    """
    language_code: Optional[str] = None
    """
    *Optional*. 
    `IETF language tag <https://en.wikipedia.org/wiki/IETF_language_tag>`_ of the user's language
    """
    is_premium: Optional[bool] = None
    """
    *Optional*. *True*, if this user is a Telegram Premium user
    """
    added_to_attachment_menu: Optional[bool] = None
    """
    *Optional*. *True*, if this user added the bot to the attachment menu
    """
    can_join_groups: Optional[bool] = None
    """
    *Optional*. *True*, if the bot can be invited to groups. 
    Returned only in :func:`sababagram.methods.get_me`.
    """
    can_read_all_group_messages: Optional[bool] = None
    """
    *Optional*. *True*, 
    if `privacy mode <https://core.telegram.org/bots/features#privacy-mode>`_ is disabled for the bot. 
    Returned only in :func:`sababagram.methods.get_me`.
    """
    supports_inline_queries: Optional[bool] = None
    """
    *Optional*. *True*, if the bot supports inline queries. 
    Returned only in :func:`sababagram.methods.get_me`.
    """
    can_connect_to_business: Optional[bool] = None
    """
    *Optional*. *True*, 
    if the bot can be connected to a Telegram Business account to receive its messages. 
    Returned only in :func:`sababagram.methods.get_me`.
    """
