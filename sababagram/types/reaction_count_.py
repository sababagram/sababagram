from dataclasses import dataclass

from .base import BaseTelegramType
from .reaction_type_ import ReactionType


@dataclass
class ReactionCount(BaseTelegramType):
    """
    Represents a reaction added to a message along with the number of times it was added.

    Source: https://core.telegram.org/bots/api#reactioncount
    """

    type: ReactionType
    """
    Type of the reaction
    """
    total_count: int
    """
    Number of times the reaction was added
    """
