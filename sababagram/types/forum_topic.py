from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class ForumTopic(BaseTelegramType):
    """
    This object represents a forum topic.

    Source: https://core.telegram.org/bots/api#forumtopic
    """

    message_thread_id: int
    """
    Unique identifier of the forum topic
    """
    name: str
    """
    Name of the topic
    """
    icon_color: int
    """
    Color of the topic icon in RGB format
    """
    icon_custom_emoji_id: Optional[str] = None
    """
    *Optional*. Unique identifier of the custom emoji shown as the topic icon
    """
