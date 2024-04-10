from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class BotCommandScope(BaseTelegramType):
    """
    This object represents the scope to which bot commands are applied. Currently,
    the following 7 scopes are supported: - :class:`sababagram.types.BotCommandScopeDefault` -
    :class:`sababagram.types.BotCommandScopeAllPrivateChats` -
    :class:`sababagram.types.BotCommandScopeAllGroupChats` -
    :class:`sababagram.types.BotCommandScopeAllChatAdministrators` -
    :class:`sababagram.types.BotCommandScopeChat` -
    :class:`sababagram.types.BotCommandScopeChatAdministrators` -
    :class:`sababagram.types.BotCommandScopeChatMember`

    Source: https://core.telegram.org/bots/api#botcommandscope
    """
