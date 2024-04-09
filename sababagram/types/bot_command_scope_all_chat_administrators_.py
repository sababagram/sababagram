from dataclasses import dataclass, field

from .bot_command_scope_ import BotCommandScope


@dataclass
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the `scope <https://core.telegram.org/bots/api#botcommandscope>`_ of bot commands,
    covering all group and supergroup chat administrators.

    Source: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    """

    type: str = field(default="all_chat_administrators", init=False)
    """
    Scope type, must be *all_chat_administrators*
    """
