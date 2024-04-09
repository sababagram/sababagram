from dataclasses import dataclass
from typing import Optional

from .input_message_content_ import InputMessageContent


@dataclass
class InputContactMessageContent(InputMessageContent):
    """
    Represents the `content <https://core.telegram.org/bots/api#inputmessagecontent>`_ of a contact
    message to be sent as the result of an inline query.

    Source: https://core.telegram.org/bots/api#inputcontactmessagecontent
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
