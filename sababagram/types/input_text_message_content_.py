from dataclasses import dataclass
from typing import Optional

from .input_message_content_ import InputMessageContent
from .link_preview_options_ import LinkPreviewOptions
from .message_entity_ import MessageEntity


@dataclass
class InputTextMessageContent(InputMessageContent):
    """
    Represents the `content <https://core.telegram.org/bots/api#inputmessagecontent>`_ of a text
    message to be sent as the result of an inline query.

    Source: https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    """
    Text of the message to be sent, 1-4096 characters
    """
    parse_mode: Optional[str] = None
    """
    *Optional*. Mode for parsing entities in the message text. 
    See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    """
    entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. List of special entities that appear in message text, 
    which can be specified instead of *parse_mode*
    """
    link_preview_options: Optional[LinkPreviewOptions] = None
    """
    *Optional*. Link preview generation options for the message
    """
