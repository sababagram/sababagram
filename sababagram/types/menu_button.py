from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class MenuButton(BaseTelegramType):
    """
    This object describes the bot's menu button in a private chat.
    It should be one of - :class:`sababagram.types.MenuButtonCommands` -
    :class:`sababagram.types.MenuButtonWebApp` - :class:`sababagram.types.MenuButtonDefault`If a menu
    button other than :class:`sababagram.types.MenuButtonDefault` is set for a private chat,
    then it is applied in the chat. Otherwise the default menu button is applied. By default,
    the menu button opens the list of bot commands.

    Source: https://core.telegram.org/bots/api#menubutton
    """
