from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class InputMessageContent(BaseTelegramType):
    """
    This object represents the content of a message to be sent as a result of an inline query.
    Telegram clients currently support the following 5 types: -
    :class:`sababagram.types.InputTextMessageContent` -
    :class:`sababagram.types.InputLocationMessageContent` -
    :class:`sababagram.types.InputVenueMessageContent` -
    :class:`sababagram.types.InputContactMessageContent` -
    :class:`sababagram.types.InputInvoiceMessageContent`

    Source: https://core.telegram.org/bots/api#inputmessagecontent
    """
