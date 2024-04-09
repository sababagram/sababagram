from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .location_ import Location


@dataclass
class Venue(BaseTelegramType):
    """
    This object represents a venue.

    Source: https://core.telegram.org/bots/api#venue
    """

    location: Location
    """
    Venue location. Can't be a live location
    """
    title: str
    """
    Name of the venue
    """
    address: str
    """
    Address of the venue
    """
    foursquare_id: Optional[str] = None
    """
    *Optional*. Foursquare identifier of the venue
    """
    foursquare_type: Optional[str] = None
    """
    *Optional*. Foursquare type of the venue. (For example, “arts_entertainment/default”, 
    “arts_entertainment/aquarium” or “food/icecream”.)
    """
    google_place_id: Optional[str] = None
    """
    *Optional*. Google Places identifier of the venue
    """
    google_place_type: Optional[str] = None
    """
    *Optional*. Google Places type of the venue. (See .)
    """
