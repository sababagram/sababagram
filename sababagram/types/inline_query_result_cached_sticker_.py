from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent


@dataclass
class InlineQueryResultCachedSticker(InlineQueryResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default,
    this sticker will be sent by the user. Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    sticker.

    Source: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """

    type: str = field(default="sticker", init=False)
    """
    Type of the result, must be *sticker*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    sticker_file_id: str
    """
    A valid file identifier of the sticker
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the sticker
    """
