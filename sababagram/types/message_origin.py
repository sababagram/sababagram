from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MessageOrigin(BaseTelegramType):
    """
    This object describes the origin of a message.
    It can be one of - :class:`sababagram.types.MessageOriginUser` -
    :class:`sababagram.types.MessageOriginHiddenUser` - :class:`sababagram.types.MessageOriginChat` -
    :class:`sababagram.types.MessageOriginChannel`

    Source: https://core.telegram.org/bots/api#messageorigin
    """
