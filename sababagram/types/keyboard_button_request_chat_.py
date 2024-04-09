from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_administrator_rights_ import ChatAdministratorRights


@dataclass
class KeyboardButtonRequestChat(BaseTelegramType):
    """
    This object defines the criteria used to request a suitable chat.
    Information about the selected chat will be shared with the bot when the corresponding button is
    pressed.
    The bot will be granted requested rights in the сhat if appropriate `More about requesting chats »
    <https://core.telegram.org/bots/features#chat-and-user-selection>`_

    Source: https://core.telegram.org/bots/api#keyboardbuttonrequestchat
    """

    request_id: int
    """
    Signed 32-bit identifier of the request, 
    which will be received back in the :class:`sababagram.types.ChatShared` object. 
    Must be unique within the message
    """
    chat_is_channel: bool
    """
    Pass *True* to request a channel chat, pass *False* to request a group or a supergroup chat.
    """
    chat_is_forum: Optional[bool] = None
    """
    *Optional*. Pass *True* to request a forum supergroup, pass *False* to request a non-forum chat. 
    If not specified, no additional restrictions are applied.
    """
    chat_has_username: Optional[bool] = None
    """
    *Optional*. Pass *True* to request a supergroup or a channel with a username, 
    pass *False* to request a chat without a username. If not specified, 
    no additional restrictions are applied.
    """
    chat_is_created: Optional[bool] = None
    """
    *Optional*. Pass *True* to request a chat owned by the user. Otherwise, 
    no additional restrictions are applied.
    """
    user_administrator_rights: Optional[ChatAdministratorRights] = None
    """
    *Optional*. 
    A JSON-serialized object listing the required administrator rights of the user in the chat. 
    The rights must be a superset of *bot_administrator_rights*. If not specified, 
    no additional restrictions are applied.
    """
    bot_administrator_rights: Optional[ChatAdministratorRights] = None
    """
    *Optional*. 
    A JSON-serialized object listing the required administrator rights of the bot in the chat. 
    The rights must be a subset of *user_administrator_rights*. If not specified, 
    no additional restrictions are applied.
    """
    bot_is_member: Optional[bool] = None
    """
    *Optional*. Pass *True* to request a chat with the bot as a member. Otherwise, 
    no additional restrictions are applied.
    """
    request_title: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the chat's title
    """
    request_username: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the chat's username
    """
    request_photo: Optional[bool] = None
    """
    *Optional*. Pass *True* to request the chat's photo
    """
