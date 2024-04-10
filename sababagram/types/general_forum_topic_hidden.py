from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class GeneralForumTopicHidden(BaseTelegramType):
    """
    This object represents a service message about General forum topic hidden in the chat.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#generalforumtopichidden
    """
