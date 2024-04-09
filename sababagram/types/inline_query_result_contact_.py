from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent


@dataclass
class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user.
    Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    contact.

    Source: https://core.telegram.org/bots/api#inlinequeryresultcontact
    """

    type: str = field(default="contact", init=False)
    """
    Type of the result, must be *contact*
    """
    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """
    phone_number: str
    """
    Contact's phone number
    """
    first_name: str
    """
    Contact's first name
    """
    last_name: Optional[str] = None
    """
    *Optional*. Contact's last name
    """
    vcard: Optional[str] = None
    """
    *Optional*. Additional data about the contact in the form of a , 0-2048 bytes
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the contact
    """
    thumbnail_url: Optional[str] = None
    """
    *Optional*. Url of the thumbnail for the result
    """
    thumbnail_width: Optional[int] = None
    """
    *Optional*. Thumbnail width
    """
    thumbnail_height: Optional[int] = None
    """
    *Optional*. Thumbnail height
    """
