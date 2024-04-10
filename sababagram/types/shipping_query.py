from dataclasses import dataclass

from . import ShippingAddress, User
from .base import BaseTelegramType


@dataclass
class ShippingQuery(BaseTelegramType):
    """
    This object contains information about an incoming shipping query.

    Source: https://core.telegram.org/bots/api#shippingquery
    """

    id: str
    """
    Unique query identifier
    """
    from_user: User
    """
    User who sent the query
    """
    invoice_payload: str
    """
    Bot specified invoice payload
    """
    shipping_address: ShippingAddress
    """
    User specified shipping address
    """
