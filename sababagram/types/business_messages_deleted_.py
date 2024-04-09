from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat


@dataclass
class BusinessMessagesDeleted(BaseTelegramType):
    """
    This object is received when messages are deleted from a connected business account.

    Source: https://core.telegram.org/bots/api#businessmessagesdeleted
    """

    business_connection_id: str
    """
    Unique identifier of the business connection
    """
    chat: Chat
    """
    Information about a chat in the business account. 
    The bot may not have access to the chat or the corresponding user.
    """
    message_ids: list[int]
    """
    A JSON-serialized list of identifiers of deleted messages in the chat of the business account
    """
