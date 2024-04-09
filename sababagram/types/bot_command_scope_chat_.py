from dataclasses import dataclass, field
from typing import Union

from .bot_command_scope_ import BotCommandScope


@dataclass
class BotCommandScopeChat(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands,
    covering a specific chat.

    Source: https://core.telegram.org/bots/api#botcommandscopechat
    """

    type: str = field(default="chat", init=False)
    """
    Scope type, must be *chat*
    """
    chat_id: Union[int, str]
    """
    Unique identifier for the target chat or username of the target supergroup (in the format 
    :code:`@supergroupusername`)
    """
