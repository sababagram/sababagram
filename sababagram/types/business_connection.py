from dataclasses import dataclass

from . import User
from .base import BaseTelegramType


@dataclass
class BusinessConnection(BaseTelegramType):
    """
    Describes the connection of the bot with a business account.

    Source: https://core.telegram.org/bots/api#businessconnection
    """

    id: str
    """
    Unique identifier of the business connection
    """
    user: User
    """
    Business account user that created the business connection
    """
    user_chat_id: int
    """
    Identifier of a private chat with the user who created the business connection. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a 64-bit integer or double-precision float type are safe for storing this identifier.
    """
    date: int
    """
    Date the connection was established in Unix time
    """
    can_reply: bool
    """
    True, 
    if the bot can act on behalf of the business account in chats that were active in the last 24 hours
    """
    is_enabled: bool
    """
    True, if the connection is active
    """
