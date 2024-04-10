from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class Birthdate(BaseTelegramType):
    """


    Source: https://core.telegram.org/bots/api#birthdate
    """

    day: int
    """
    Day of the user's birth; 1-31
    """
    month: int
    """
    Month of the user's birth; 1-12
    """
    year: Optional[int] = None
    """
    *Optional*. Year of the user's birth
    """
