from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat


@dataclass
class InaccessibleMessage(BaseTelegramType):
    """
    This object describes a message that was deleted or is otherwise inaccessible to the bot.

    Source: https://core.telegram.org/bots/api#inaccessiblemessage
    """

    chat: Chat
    """
    Chat the message belonged to
    """
    message_id: int
    """
    Unique message identifier inside the chat
    """
    date: int
    """
    Always 0. The field can be used to differentiate regular and inaccessible messages.
    """
