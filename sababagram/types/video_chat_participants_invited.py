from dataclasses import dataclass

from . import User
from .base import BaseTelegramType


@dataclass
class VideoChatParticipantsInvited(BaseTelegramType):
    """
    This object represents a service message about new members invited to a video chat.

    Source: https://core.telegram.org/bots/api#videochatparticipantsinvited
    """

    users: list[User]
    """
    New members that were invited to the video chat
    """
