from dataclasses import dataclass, field
from typing import Optional

from . import InlineKeyboardMarkup, InlineQueryResult, InputMessageContent, MessageEntity


@dataclass
class InlineQueryResultCachedAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default,
    this audio file will be sent by the user. Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    audio.

    Source: https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """

    type: str = field(default="audio", init=False)
    """
    Type of the result, must be *audio*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    audio_file_id: str
    """
    A valid file identifier for the audio file
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
