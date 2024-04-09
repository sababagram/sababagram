from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .message_ import Message


@dataclass
class GiveawayCompleted(BaseTelegramType):
    """
    This object represents a service message about the completion of a giveaway without public winners.

    Source: https://core.telegram.org/bots/api#giveawaycompleted
    """

    winner_count: int
    """
    Number of winners in the giveaway
    """
    unclaimed_prize_count: Optional[int] = None
    """
    *Optional*. Number of undistributed prizes
    """
    giveaway_message: Optional[Message] = None
    """
    *Optional*. Message with the giveaway that was completed, if it wasn't deleted
    """
