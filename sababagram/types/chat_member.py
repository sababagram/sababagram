from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ChatMember(BaseTelegramType):
    """
    This object contains information about one member of a chat. Currently,
    the following 6 types of chat members are supported: - :class:`sababagram.types.ChatMemberOwner` -
    :class:`sababagram.types.ChatMemberAdministrator` - :class:`sababagram.types.ChatMemberMember` -
    :class:`sababagram.types.ChatMemberRestricted` - :class:`sababagram.types.ChatMemberLeft` -
    :class:`sababagram.types.ChatMemberBanned`

    Source: https://core.telegram.org/bots/api#chatmember
    """
