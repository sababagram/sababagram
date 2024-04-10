from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class CallbackGame(BaseTelegramType):
    """
    A placeholder, currently holds no information.
    Use `BotFather <https://t.me/botfather>`_ to set up your game.

    Source: https://core.telegram.org/bots/api#callbackgame
    """
