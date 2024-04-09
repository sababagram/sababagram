from dataclasses import dataclass, field
from typing import Union

from .bot_command_scope_ import BotCommandScope


@dataclass
class BotCommandScopeChatAdministrators(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands,
    covering all administrators of a specific group or supergroup chat.

    Source: https://core.telegram.org/bots/api#botcommandscopechatadministrators
    """

    type: str = field(default="chat_administrators", init=False)
    """
    Scope type, must be *chat_administrators*
    """
    chat_id: Union[int, str]
    """
    Unique identifier for the target chat or username of the target supergroup (in the format 
    :code:`@supergroupusername`)
    """
