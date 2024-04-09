from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .chat_ import Chat
from .user_ import User


@dataclass
class PollAnswer(BaseTelegramType):
    """
    This object represents an answer of a user in a non-anonymous poll.

    Source: https://core.telegram.org/bots/api#pollanswer
    """

    poll_id: str
    """
    Unique poll identifier
    """
    option_ids: list[int]
    """
    0-based identifiers of chosen answer options. May be empty if the vote was retracted.
    """
    voter_chat: Optional[Chat] = None
    """
    *Optional*. The chat that changed the answer to the poll, if the voter is anonymous
    """
    user: Optional[User] = None
    """
    *Optional*. The user that changed the answer to the poll, if the voter isn't anonymous
    """
