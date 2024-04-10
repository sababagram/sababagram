from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MaybeInaccessibleMessage(BaseTelegramType):
    """
    This object describes a message that can be inaccessible to the bot.
    It can be one of - :class:`sababagram.types.Message` -
    :class:`sababagram.types.InaccessibleMessage`

    Source: https://core.telegram.org/bots/api#maybeinaccessiblemessage
    """
