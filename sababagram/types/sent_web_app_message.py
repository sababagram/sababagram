from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class SentWebAppMessage(BaseTelegramType):
    """
    Describes an inline message sent by a `Web App <https://core.telegram.org/bots/webapps>`_ on
    behalf of a user.

    Source: https://core.telegram.org/bots/api#sentwebappmessage
    """

    inline_message_id: Optional[str] = None
    """
    *Optional*. Identifier of the sent inline message. 
    Available only if there is an `inline keyboard 
    <https://core.telegram.org/bots/api#inlinekeyboardmarkup>`_ attached to the message.
    """
