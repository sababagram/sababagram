from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .callback_game_ import CallbackGame
from .login_url_ import LoginUrl
from .switch_inline_query_chosen_chat_ import SwitchInlineQueryChosenChat
from .web_app_info_ import WebAppInfo


@dataclass
class InlineKeyboardButton(BaseTelegramType):
    """
    This object represents one button of an inline keyboard.
    You **must** use exactly one of the optional fields.

    Source: https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    """
    Label text on the button
    """
    url: Optional[str] = None
    """
    *Optional*. HTTP or tg:// URL to be opened when the button is pressed. 
    Links :code:`tg://user?id=<user_id>` can be used to mention a user by their identifier without 
    using a username, if this is allowed by their privacy settings.
    """
    callback_data: Optional[str] = None
    """
    *Optional*. 
    Data to be sent in a `callback query <https://core.telegram.org/bots/api#callbackquery>`_ to the 
    bot when button is pressed, 1-64 bytes
    """
    web_app: Optional[WebAppInfo] = None
    """
    *Optional*. 
    Description of the `Web App <https://core.telegram.org/bots/webapps>`_ that will be launched when 
    the user presses the button. 
    The Web App will be able to send an arbitrary message on behalf of the user using the method 
    :func:`sababagram.methods.answer_web_app_query`. 
    Available only in private chats between a user and the bot.
    """
    login_url: Optional[LoginUrl] = None
    """
    *Optional*. An HTTPS URL used to automatically authorize the user. 
    Can be used as a replacement for the `Telegram Login Widget 
    <https://core.telegram.org/widgets/login>`_.
    """
    switch_inline_query: Optional[str] = None
    """
    *Optional*. If set, pressing the button will prompt the user to select one of their chats, 
    open that chat and insert the bot's username and the specified inline query in the input field. 
    May be empty, in which case just the bot's username will be inserted.
    """
    switch_inline_query_current_chat: Optional[str] = None
    """
    *Optional*. If set, 
    pressing the button will insert the bot's username and the specified inline query in the current 
    chat's input field. May be empty, in which case only the bot's username will be inserted.
    
    This offers a quick way for the user to open your bot in inline mode in the same chat - good for 
    selecting something from multiple options.
    """
    switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None
    """
    *Optional*. If set, 
    pressing the button will prompt the user to select one of their chats of the specified type, 
    open that chat and insert the bot's username and the specified inline query in the input field
    """
    callback_game: Optional[CallbackGame] = None
    """
    *Optional*. Description of the game that will be launched when the user presses the button.
    
    **NOTE:** This type of button **must** always be the first button in the first row.
    """
    pay: Optional[bool] = None
    """
    *Optional*. Specify *True*, to send a `Pay button <https://core.telegram.org/bots/api#payments>`_.
    
    **NOTE:** This type of button **must** always be the first button in the first row and can only be 
    used in invoice messages.
    """
