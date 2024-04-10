from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ShippingAddress(BaseTelegramType):
    """
    This object represents a shipping address.

    Source: https://core.telegram.org/bots/api#shippingaddress
    """

    country_code: str
    """
    Two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ country code
    """
    state: str
    """
    State, if applicable
    """
    city: str
    """
    City
    """
    street_line1: str
    """
    First line for the address
    """
    street_line2: str
    """
    Second line for the address
    """
    post_code: str
    """
    Address post code
    """
