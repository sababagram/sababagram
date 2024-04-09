from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ForumTopicReopened(BaseTelegramType):
    """
    This object represents a service message about a forum topic reopened in the chat.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#forumtopicreopened
    """
