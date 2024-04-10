from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class GiveawayCreated(BaseTelegramType):
    """
    This object represents a service message about the creation of a scheduled giveaway.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#giveawaycreated
    """
