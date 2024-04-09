from dataclasses import dataclass
from typing import Optional

from .animation_ import Animation
from .base import BaseTelegramType
from .message_entity_ import MessageEntity
from .photo_size_ import PhotoSize


@dataclass
class Game(BaseTelegramType):
    """
    This object represents a game. Use BotFather to create and edit games,
    their short names will act as unique identifiers.

    Source: https://core.telegram.org/bots/api#game
    """

    title: str
    """
    Title of the game
    """
    description: str
    """
    Description of the game
    """
    photo: list[PhotoSize]
    """
    Photo that will be displayed in the game message in chats.
    """
    text: Optional[str] = None
    """
    *Optional*. Brief description of the game or high scores included in the game message. 
    Can be automatically edited to include current high scores for the game when the bot calls 
    :func:`sababagram.methods.set_game_score`, 
    or manually edited using :func:`sababagram.methods.edit_message_text`. 0-4096 characters.
    """
    text_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc.
    """
    animation: Optional[Animation] = None
    """
    *Optional*. Animation that will be displayed in the game message in chats. Upload via 
    """
