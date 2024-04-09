from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .location_ import Location


@dataclass
class BusinessLocation(BaseTelegramType):
    """


    Source: https://core.telegram.org/bots/api#businesslocation
    """

    address: str
    """
    Address of the business
    """
    location: Optional[Location] = None
    """
    *Optional*. Location of the business
    """
