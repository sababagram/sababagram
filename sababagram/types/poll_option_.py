from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class PollOption(BaseTelegramType):
    """
    This object contains information about one answer option in a poll.

    Source: https://core.telegram.org/bots/api#polloption
    """

    text: str
    """
    Option text, 1-100 characters
    """
    voter_count: int
    """
    Number of users that voted for this option
    """
