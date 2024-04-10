from dataclasses import dataclass

from . import InlineKeyboardButton
from .base import BaseTelegramType


@dataclass
class InlineKeyboardMarkup(BaseTelegramType):
    """
    This object represents an `inline keyboard
    <https://core.telegram.org/bots/features#inline-keyboards>`_ that appears right next to the
    message it belongs to.

    Source: https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: list[list[InlineKeyboardButton]]
    """
    Array of button rows, 
    each represented by an Array of :class:`sababagram.types.InlineKeyboardButton` objects
    """
