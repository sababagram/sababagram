from dataclasses import dataclass

from .base import BaseTelegramType
from .shared_user_ import SharedUser


@dataclass
class UsersShared(BaseTelegramType):
    """
    This object contains information about the users whose identifiers were shared with the bot using
    a :class:`sababagram.types.KeyboardButtonRequestUsers` button.

    Source: https://core.telegram.org/bots/api#usersshared
    """

    request_id: int
    """
    Identifier of the request
    """
    users: list[SharedUser]
    """
    Information about users shared with the bot.
    """
