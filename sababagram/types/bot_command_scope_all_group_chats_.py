from dataclasses import dataclass, field

from .bot_command_scope_ import BotCommandScope


@dataclass
class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands,
    covering all group and supergroup chats.

    Source: https://core.telegram.org/bots/api#botcommandscopeallgroupchats
    """

    type: str = field(default="all_group_chats", init=False)
    """
    Scope type, must be *all_group_chats*
    """
