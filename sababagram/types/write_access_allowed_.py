from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class WriteAccessAllowed(BaseTelegramType):
    """
    This object represents a service message about a user allowing a bot to write messages after
    adding it to the attachment menu, launching a Web App from a link,
    or accepting an explicit request from a Web App sent by the method `requestWriteAccess
    <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_.

    Source: https://core.telegram.org/bots/api#writeaccessallowed
    """

    from_request: Optional[bool] = None
    """
    *Optional*. True, 
    if the access was granted after the user accepted an explicit request from a Web App sent by the 
    method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_
    """
    web_app_name: Optional[str] = None
    """
    *Optional*. Name of the Web App, 
    if the access was granted when the Web App was launched from a link
    """
    from_attachment_menu: Optional[bool] = None
    """
    *Optional*. True, if the access was granted when the bot was added to the attachment or side menu
    """
