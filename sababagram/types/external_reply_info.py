from dataclasses import dataclass
from typing import Optional

from . import (
    Animation,
    Audio,
    Chat,
    Contact,
    Dice,
    Document,
    Game,
    Giveaway,
    GiveawayWinners,
    Invoice,
    LinkPreviewOptions,
    Location,
    MessageOrigin,
    PhotoSize,
    Poll,
    Sticker,
    Story,
    Venue,
    Video,
    VideoNote,
    Voice,
)
from .base import BaseTelegramType


@dataclass
class ExternalReplyInfo(BaseTelegramType):
    """
    This object contains information about a message that is being replied to,
    which may come from another chat or forum topic.

    Source: https://core.telegram.org/bots/api#externalreplyinfo
    """

    origin: MessageOrigin
    """
    Origin of the message replied to by the given message
    """
    chat: Optional[Chat] = None
    """
    *Optional*. Chat the original message belongs to. 
    Available only if the chat is a supergroup or a channel.
    """
    message_id: Optional[int] = None
    """
    *Optional*. Unique message identifier inside the original chat. 
    Available only if the original chat is a supergroup or a channel.
    """
    link_preview_options: Optional[LinkPreviewOptions] = None
    """
    *Optional*. Options used for link preview generation for the original message, 
    if it is a text message
    """
    animation: Optional[Animation] = None
    """
    *Optional*. Message is an animation, information about the animation
    """
    audio: Optional[Audio] = None
    """
    *Optional*. Message is an audio file, information about the file
    """
    document: Optional[Document] = None
    """
    *Optional*. Message is a general file, information about the file
    """
    photo: Optional[list[PhotoSize]] = None
    """
    *Optional*. Message is a photo, available sizes of the photo
    """
    sticker: Optional[Sticker] = None
    """
    *Optional*. Message is a sticker, information about the sticker
    """
    story: Optional[Story] = None
    """
    *Optional*. Message is a forwarded story
    """
    video: Optional[Video] = None
    """
    *Optional*. Message is a video, information about the video
    """
    video_note: Optional[VideoNote] = None
    """
    *Optional*. Message is a `video note <https://telegram.org/blog/video-messages-and-telescope>`_, 
    information about the video message
    """
    voice: Optional[Voice] = None
    """
    *Optional*. Message is a voice message, information about the file
    """
    has_media_spoiler: Optional[bool] = None
    """
    *Optional*. *True*, if the message media is covered by a spoiler animation
    """
    contact: Optional[Contact] = None
    """
    *Optional*. Message is a shared contact, information about the contact
    """
    dice: Optional[Dice] = None
    """
    *Optional*. Message is a dice with random value
    """
    game: Optional[Game] = None
    """
    *Optional*. Message is a game, information about the game. 
    `More about games » <https://core.telegram.org/bots/api#games>`_
    """
    giveaway: Optional[Giveaway] = None
    """
    *Optional*. Message is a scheduled giveaway, information about the giveaway
    """
    giveaway_winners: Optional[GiveawayWinners] = None
    """
    *Optional*. A giveaway with public winners was completed
    """
    invoice: Optional[Invoice] = None
    """
    *Optional*. Message is an invoice for a `payment <https://core.telegram.org/bots/api#payments>`_, 
    information about the invoice. 
    `More about payments » <https://core.telegram.org/bots/api#payments>`_
    """
    location: Optional[Location] = None
    """
    *Optional*. Message is a shared location, information about the location
    """
    poll: Optional[Poll] = None
    """
    *Optional*. Message is a native poll, information about the poll
    """
    venue: Optional[Venue] = None
    """
    *Optional*. Message is a venue, information about the venue
    """
