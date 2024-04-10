from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class KeyboardButtonRequestUsers(BaseTelegramType):
    """
    This object defines the criteria used to request suitable users.
    Information about the selected users will be shared with the bot when the corresponding button is
    pressed.
    `More about requesting users » <https://core.telegram.org/bots/features#chat-and-user-selection>`_

    Source: https://core.telegram.org/bots/api#keyboardbuttonrequestusers
    """

    request_id: int
    """
    Signed 32-bit identifier of the request that will be received back in the 
    :class:`sababagram.types.UsersShared` object. Must be unique within the message
    """
    user_is_bot: Optional[bool] = None
    """
    *Optional*. Pass *True* to request bots, pass *False* to request regular users. If not specified, 
    no additional restrictions are applied.
    """
    user_is_premium: Optional[bool] = None
    """
    *Optional*. Pass *True* to request premium users, pass *False* to request non-premium users. 
    If not specified, no additional restrictions are applied.
    """
    max_quantity: Optional[int] = None
    """
    *Optional*. The maximum number of users to be selected; 1-10. Defaults to 1.
    """
    request_name: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the users' first and last name
    """
    request_username: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the users' username
    """
    request_photo: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the users' photo
    """
