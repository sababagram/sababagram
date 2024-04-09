from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .keyboard_button_poll_type_ import KeyboardButtonPollType
from .keyboard_button_request_chat_ import KeyboardButtonRequestChat
from .keyboard_button_request_users_ import KeyboardButtonRequestUsers
from .web_app_info_ import WebAppInfo


@dataclass
class KeyboardButton(BaseTelegramType):
    """
    This object represents one button of the reply keyboard. For simple text buttons,
    *String* can be used instead of this object to specify the button text.
    The optional fields *web_app*, *request_users*, *request_chat*, *request_contact*,
    *request_location*,
    and *request_poll* are mutually exclusive.**Note:** *request_users* and *request_chat* options
    will only work in Telegram versions released after 3 February, 2023.
    Older clients will display *unsupported message*.

    Source: https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    """
    Text of the button. If none of the optional fields are used, 
    it will be sent as a message when the button is pressed
    """
    request_users: Optional[KeyboardButtonRequestUsers] = None
    """
    *Optional.* If specified, pressing the button will open a list of suitable users. 
    Identifiers of selected users will be sent to the bot in a “users_shared” service message. 
    Available in private chats only.
    """
    request_chat: Optional[KeyboardButtonRequestChat] = None
    """
    *Optional.* If specified, pressing the button will open a list of suitable chats. 
    Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. 
    Available in private chats only.
    """
    request_contact: Optional[bool] = None
    """
    *Optional*. If *True*, 
    the user's phone number will be sent as a contact when the button is pressed. 
    Available in private chats only.
    """
    request_location: Optional[bool] = None
    """
    *Optional*. If *True*, the user's current location will be sent when the button is pressed. 
    Available in private chats only.
    """
    request_poll: Optional[KeyboardButtonPollType] = None
    """
    *Optional*. If specified, 
    the user will be asked to create a poll and send it to the bot when the button is pressed. 
    Available in private chats only.
    """
    web_app: Optional[WebAppInfo] = None
    """
    *Optional*. If specified, 
    the described `Web App <https://core.telegram.org/bots/webapps>`_ will be launched when the button 
    is pressed. The Web App will be able to send a “web_app_data” service message. 
    Available in private chats only.
    """
