from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ForumTopicClosed(BaseTelegramType):
    """
    This object represents a service message about a forum topic closed in the chat.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#forumtopicclosed
    """
