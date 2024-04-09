from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class VideoChatEnded(BaseTelegramType):
    """
    This object represents a service message about a video chat ended in the chat.

    Source: https://core.telegram.org/bots/api#videochatended
    """

    duration: int
    """
    Video chat duration in seconds
    """
