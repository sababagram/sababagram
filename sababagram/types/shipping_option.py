from dataclasses import dataclass

from . import LabeledPrice
from .base import BaseTelegramType


@dataclass
class ShippingOption(BaseTelegramType):
    """
    This object represents one shipping option.

    Source: https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    """
    Shipping option identifier
    """
    title: str
    """
    Option title
    """
    prices: list[LabeledPrice]
    """
    List of price portions
    """
