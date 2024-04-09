from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult


@dataclass
class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a `Game <https://core.telegram.org/bots/api#games>`_.

    Source: https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    type: str = field(default="game", init=False)
    """
    Type of the result, must be *game*
    """
    id: str
    """
    Unique identifier for this result, 1-64 bytes
    """
    game_short_name: str
    """
    Short name of the game
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
