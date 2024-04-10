from dataclasses import dataclass
from typing import Optional

from . import ShippingAddress
from .base import BaseTelegramType


@dataclass
class OrderInfo(BaseTelegramType):
    """
    This object represents information about an order.

    Source: https://core.telegram.org/bots/api#orderinfo
    """

    name: Optional[str] = None
    """
    *Optional*. User name
    """
    phone_number: Optional[str] = None
    """
    *Optional*. User's phone number
    """
    email: Optional[str] = None
    """
    *Optional*. User email
    """
    shipping_address: Optional[ShippingAddress] = None
    """
    *Optional*. User shipping address
    """
