from dataclasses import dataclass

from . import BusinessOpeningHoursInterval
from .base import BaseTelegramType


@dataclass
class BusinessOpeningHours(BaseTelegramType):
    """


    Source: https://core.telegram.org/bots/api#businessopeninghours
    """

    time_zone_name: str
    """
    Unique name of the time zone for which the opening hours are defined
    """
    opening_hours: list[BusinessOpeningHoursInterval]
    """
    List of time intervals describing business opening hours
    """
