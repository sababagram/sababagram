from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .photo_size_ import PhotoSize


@dataclass
class VideoNote(BaseTelegramType):
    """
    This object represents a  (available in Telegram apps as of ).

    Source: https://core.telegram.org/bots/api#videonote
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, 
    which is supposed to be the same over time and for different bots. 
    Can't be used to download or reuse the file.
    """
    length: int
    """
    Video width and height (diameter of the video message) as defined by sender
    """
    duration: int
    """
    Duration of the video in seconds as defined by sender
    """
    thumbnail: Optional[PhotoSize] = None
    """
    *Optional*. Video thumbnail
    """
    file_size: Optional[int] = None
    """
    *Optional*. File size in bytes
    """
