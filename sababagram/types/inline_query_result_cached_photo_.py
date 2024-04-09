from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent
from .message_entity_ import MessageEntity


@dataclass
class InlineQueryResultCachedPhoto(InlineQueryResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default,
    this photo will be sent by the user with an optional caption. Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    photo.

    Source: https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """

    type: str = field(default="photo", init=False)
    """
    Type of the result, must be *photo*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    photo_file_id: str
    """
    A valid file identifier of the photo
    """
    title: Optional[str] = None
    """
    *Optional*. Title for the result
    """
    description: Optional[str] = None
    """
    *Optional*. Short description of the result
    """
    caption: Optional[str] = None
    """
    *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing
    """
    parse_mode: Optional[str] = None
    """
    *Optional*. Mode for parsing entities in the photo caption. 
    See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    """
    caption_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. List of special entities that appear in the caption, 
    which can be specified instead of *parse_mode*
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the photo
    """
