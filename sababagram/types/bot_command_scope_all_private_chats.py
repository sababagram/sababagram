from dataclasses import dataclass, field

from . import BotCommandScope


@dataclass
class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands,
    covering all private chats.

    Source: https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    """

    type: str = field(default="all_private_chats", init=False)
    """
    Scope type, must be *all_private_chats*
    """
