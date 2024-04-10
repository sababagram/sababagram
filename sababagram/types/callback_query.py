from dataclasses import dataclass
from typing import Optional, Union

from . import InaccessibleMessage, Message, User
from .base import BaseTelegramType


@dataclass
class CallbackQuery(BaseTelegramType):
    """
    This object represents an incoming callback query from a callback button in an `inline keyboard
    <https://core.telegram.org/bots/features#inline-keyboards>`_.
    If the button that originated the query was attached to a message sent by the bot,
    the field *message* will be present.
    If the button was attached to a message sent via the bot (in `inline mode
    <https://core.telegram.org/bots/api#inline-mode>`_),
    the field *inline_message_id* will be present.
    Exactly one of the fields *data* or *game_short_name* will be present.

     **NOTE:** After the user presses a callback button,
     Telegram clients will display a progress bar until you call
     :func:`sababagram.methods.answer_callback_query`. It is, therefore,
     necessary to react by calling :func:`sababagram.methods.answer_callback_query` even if no
     notification to the user is needed (e.g., without specifying any of the optional parameters).


    Source: https://core.telegram.org/bots/api#callbackquery
    """

    id: str
    """
    Unique identifier for this query
    """
    from_user: User
    """
    Sender
    """
    chat_instance: str
    """
    Global identifier, 
    uniquely corresponding to the chat to which the message with the callback button was sent. 
    Useful for high scores in :func:`sababagram.methods.games`.
    """
    message: Optional[Union[Message, InaccessibleMessage]] = None
    """
    *Optional*. Message sent by the bot with the callback button that originated the query
    """
    inline_message_id: Optional[str] = None
    """
    *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query.
    """
    data: Optional[str] = None
    """
    *Optional*. Data associated with the callback button. 
    Be aware that the message originated the query can contain no callback buttons with this data.
    """
    game_short_name: Optional[str] = None
    """
    *Optional*. Short name of a `Game <https://core.telegram.org/bots/api#games>`_ to be returned, 
    serves as the unique identifier for the game
    """
