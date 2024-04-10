from dataclasses import dataclass, field
from typing import Optional

from . import InlineKeyboardMarkup, InlineQueryResult, InputMessageContent, MessageEntity


@dataclass
class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default,
    this voice recording will be sent by the user. Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    the voice message.

    Source: https://core.telegram.org/bots/api#inlinequeryresultvoice
    """

    type: str = field(default="voice", init=False)
    """
    Type of the result, must be *voice*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    voice_url: str
    """
    A valid URL for the voice recording
    """
    title: str
    """
    Recording title
    """
    caption: Optional[str] = None
    """
    *Optional*. Caption, 0-1024 characters after entities parsing
    """
    parse_mode: Optional[str] = None
    """
    *Optional*. Mode for parsing entities in the voice message caption. 
    See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    """
    caption_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. List of special entities that appear in the caption, 
    which can be specified instead of *parse_mode*
    """
    voice_duration: Optional[int] = None
    """
    *Optional*. Recording duration in seconds
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the voice recording
    """
