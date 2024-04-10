from dataclasses import dataclass

from . import Chat
from .base import BaseTelegramType


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
