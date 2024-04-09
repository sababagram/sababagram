from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent


@dataclass
class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively,
    you can use *input_message_content* to send a message with the specified content instead of the
    venue.

    Source: https://core.telegram.org/bots/api#inlinequeryresultvenue
    """

    type: str = field(default="venue", init=False)
    """
    Type of the result, must be *venue*
    """
    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """
    latitude: float
    """
    Latitude of the venue location in degrees
    """
    longitude: float
    """
    Longitude of the venue location in degrees
    """
    title: str
    """
    Title of the venue
    """
    address: str
    """
    Address of the venue
    """
    foursquare_id: Optional[str] = None
    """
    *Optional*. Foursquare identifier of the venue if known
    """
    foursquare_type: Optional[str] = None
    """
    *Optional*. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, 
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
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    input_message_content: Optional[InputMessageContent] = None
    """
    *Optional*. Content of the message to be sent instead of the venue
    """
    thumbnail_url: Optional[str] = None
    """
    *Optional*. Url of the thumbnail for the result
    """
    thumbnail_width: Optional[int] = None
    """
    *Optional*. Thumbnail width
    """
    thumbnail_height: Optional[int] = None
    """
    *Optional*. Thumbnail height
    """
