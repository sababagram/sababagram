from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ChatBoostSource(BaseTelegramType):
    """
    This object describes the source of a chat boost.
    It can be one of - :class:`sababagram.types.ChatBoostSourcePremium` -
    :class:`sababagram.types.ChatBoostSourceGiftCode` -
    :class:`sababagram.types.ChatBoostSourceGiveaway`

    Source: https://core.telegram.org/bots/api#chatboostsource
    """
