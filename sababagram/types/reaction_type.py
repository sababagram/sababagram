from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ReactionType(BaseTelegramType):
    """
    This object describes the type of a reaction. Currently,
    it can be one of - :class:`sababagram.types.ReactionTypeEmoji` -
    :class:`sababagram.types.ReactionTypeCustomEmoji`

    Source: https://core.telegram.org/bots/api#reactiontype
    """
