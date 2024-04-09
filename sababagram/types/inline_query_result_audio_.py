from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent
from .message_entity_ import MessageEntity


@dataclass
class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user.
    Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    audio.

    Source: https://core.telegram.org/bots/api#inlinequeryresultaudio
    """

    type: str = field(default="audio", init=False)
    """
    Type of the result, must be *audio*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    audio_url: str
    """
    A valid URL for the audio file
    """
    title: str
    """
    Title
    """
    caption: Optional[str] = None
    """
    *Optional*. Caption, 0-1024 characters after entities parsing
    """
    parse_mode: Optional[str] = None
    """
    *Optional*. Mode for parsing entities in the audio caption. 
    See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    """
    caption_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. List of special entities that appear in the caption, 
    which can be specified instead of *parse_mode*
    """
    performer: Optional[str] = None
    """
    *Optional*. Performer
    """
    audio_duration: Optional[int] = None
    """
    *Optional*. Audio duration in seconds
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the audio
    """
