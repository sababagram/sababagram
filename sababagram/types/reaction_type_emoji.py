from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class ReactionTypeEmoji(BaseTelegramType):
    """
    The reaction is based on an emoji.

    Source: https://core.telegram.org/bots/api#reactiontypeemoji
    """

    type: str
    """
    Type of the reaction, always “emoji”
    """
    emoji: str
    """
    Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", 
    "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", 
    "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", 
    "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", 
    "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"
    """
