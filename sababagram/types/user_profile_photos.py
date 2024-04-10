from dataclasses import dataclass

from . import PhotoSize
from .base import BaseTelegramType


@dataclass
class UserProfilePhotos(BaseTelegramType):
    """
    This object represent a user's profile pictures.

    Source: https://core.telegram.org/bots/api#userprofilephotos
    """

    total_count: int
    """
    Total number of profile pictures the target user has
    """
    photos: list[list[PhotoSize]]
    """
    Requested profile pictures (in up to 4 sizes each)
    """
