from dataclasses import dataclass

from .base import BaseTelegramType
from .inline_keyboard_button_ import InlineKeyboardButton


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
