from dataclasses import dataclass

from .base import BaseTelegramType
from .chat_ import Chat


@dataclass
class Story(BaseTelegramType):
    """
    This object represents a story.

    Source: https://core.telegram.org/bots/api#story
    """

    chat: Chat
    """
    Chat that posted the story
    """
    id: int
    """
    Unique identifier for the story in the chat
    """
