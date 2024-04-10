from dataclasses import dataclass

from . import User
from .base import BaseTelegramType


@dataclass
class GameHighScore(BaseTelegramType):
    """
    This object represents one row of the high scores table for a game.And that's about all we've got
    for now.
    If you've got any questions, please check out our `Bot FAQ » <https://core.telegram.org/bots/faq>`_

    Source: https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    """
    Position in high score table for the game
    """
    user: User
    """
    User
    """
    score: int
    """
    Score
    """
