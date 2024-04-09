from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .photo_size_ import PhotoSize
from .sticker_ import Sticker


@dataclass
class StickerSet(BaseTelegramType):
    """
    This object represents a sticker set.

    Source: https://core.telegram.org/bots/api#stickerset
    """

    name: str
    """
    Sticker set name
    """
    title: str
    """
    Sticker set title
    """
    sticker_type: str
    """
    Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”
    """
    stickers: list[Sticker]
    """
    List of all set stickers
    """
    thumbnail: Optional[PhotoSize] = None
    """
    *Optional*. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    """
