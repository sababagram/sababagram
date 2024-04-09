from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class GeneralForumTopicUnhidden(BaseTelegramType):
    """
    This object represents a service message about General forum topic unhidden in the chat.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#generalforumtopicunhidden
    """
