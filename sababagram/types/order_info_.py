from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .shipping_address_ import ShippingAddress


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
