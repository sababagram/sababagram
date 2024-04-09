from dataclasses import dataclass

from .base import BaseTelegramType
from .shipping_address_ import ShippingAddress
from .user_ import User


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
