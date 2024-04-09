from dataclasses import dataclass

from .base import BaseTelegramType
from .business_opening_hours_interval_ import BusinessOpeningHoursInterval


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
