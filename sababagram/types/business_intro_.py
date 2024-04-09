from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .sticker_ import Sticker


@dataclass
class BusinessIntro(BaseTelegramType):
    """


    Source: https://core.telegram.org/bots/api#businessintro
    """

    title: Optional[str] = None
    """
    *Optional*. Title text of the business intro
    """
    message: Optional[str] = None
    """
    *Optional*. Message text of the business intro
    """
    sticker: Optional[Sticker] = None
    """
    *Optional*. Sticker of the business intro
    """
