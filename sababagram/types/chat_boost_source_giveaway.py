from dataclasses import dataclass
from typing import Optional

from . import User
from .base import BaseTelegramType


@dataclass
class ChatBoostSourceGiveaway(BaseTelegramType):
    """
    The boost was obtained by the creation of a Telegram Premium giveaway.
    This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

    Source: https://core.telegram.org/bots/api#chatboostsourcegiveaway
    """

    source: str
    """
    Source of the boost, always “giveaway”
    """
    giveaway_message_id: int
    """
    Identifier of a message in the chat with the giveaway; 
    the message could have been deleted already. May be 0 if the message isn't sent yet.
    """
    user: Optional[User] = None
    """
    *Optional*. User that won the prize in the giveaway if any
    """
    is_unclaimed: Optional[bool] = None
    """
    *Optional*. True, if the giveaway was completed, but there was no user to win the prize
    """
