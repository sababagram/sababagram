from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class InputMedia(BaseTelegramType):
    """
    This object represents the content of a media message to be sent.
    It should be one of - :class:`sababagram.types.InputMediaAnimation` -
    :class:`sababagram.types.InputMediaDocument` - :class:`sababagram.types.InputMediaAudio` -
    :class:`sababagram.types.InputMediaPhoto` - :class:`sababagram.types.InputMediaVideo`

    Source: https://core.telegram.org/bots/api#inputmedia
    """
