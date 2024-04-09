from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_ import Chat
from .user_ import User


@dataclass
class GiveawayWinners(BaseTelegramType):
    """
    This object represents a message about the completion of a giveaway with public winners.

    Source: https://core.telegram.org/bots/api#giveawaywinners
    """

    chat: Chat
    """
    The chat that created the giveaway
    """
    giveaway_message_id: int
    """
    Identifier of the message with the giveaway in the chat
    """
    winners_selection_date: int
    """
    Point in time (Unix timestamp) when winners of the giveaway were selected
    """
    winner_count: int
    """
    Total number of winners in the giveaway
    """
    winners: list[User]
    """
    List of up to 100 winners of the giveaway
    """
    additional_chat_count: Optional[int] = None
    """
    *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway
    """
    premium_subscription_month_count: Optional[int] = None
    """
    *Optional*. 
    The number of months the Telegram Premium subscription won from the giveaway will be active for
    """
    unclaimed_prize_count: Optional[int] = None
    """
    *Optional*. Number of undistributed prizes
    """
    only_new_members: Optional[bool] = None
    """
    *Optional*. *True*, 
    if only users who had joined the chats after the giveaway started were eligible to win
    """
    was_refunded: Optional[bool] = None
    """
    *Optional*. *True*, if the giveaway was canceled because the payment for it was refunded
    """
    prize_description: Optional[str] = None
    """
    *Optional*. Description of additional giveaway prize
    """
