from dataclasses import dataclass
from typing import Optional, Union

from . import (
    Animation,
    Audio,
    Chat,
    ChatBoostAdded,
    ChatShared,
    Contact,
    Dice,
    Document,
    ExternalReplyInfo,
    ForumTopicClosed,
    ForumTopicCreated,
    ForumTopicEdited,
    ForumTopicReopened,
    Game,
    GeneralForumTopicHidden,
    GeneralForumTopicUnhidden,
    Giveaway,
    GiveawayCompleted,
    GiveawayCreated,
    GiveawayWinners,
    InaccessibleMessage,
    InlineKeyboardMarkup,
    Invoice,
    LinkPreviewOptions,
    Location,
    MessageAutoDeleteTimerChanged,
    MessageEntity,
    MessageOrigin,
    PassportData,
    PhotoSize,
    Poll,
    ProximityAlertTriggered,
    Sticker,
    Story,
    SuccessfulPayment,
    TextQuote,
    User,
    UsersShared,
    Venue,
    Video,
    VideoChatEnded,
    VideoChatParticipantsInvited,
    VideoChatScheduled,
    VideoChatStarted,
    VideoNote,
    Voice,
    WebAppData,
    WriteAccessAllowed,
)
from .base import BaseTelegramType


@dataclass
class Message(BaseTelegramType):
    """
    This object represents a message.

    Source: https://core.telegram.org/bots/api#message
    """

    message_id: int
    """
    Unique message identifier inside this chat
    """
    date: int
    """
    Date the message was sent in Unix time. It is always a positive number, representing a valid date.
    """
    chat: Chat
    """
    Chat the message belongs to
    """
    message_thread_id: Optional[int] = None
    """
    *Optional*. Unique identifier of a message thread to which the message belongs; 
    for supergroups only
    """
    from_user: Optional[User] = None
    """
    *Optional*. Sender of the message; empty for messages sent to channels. 
    For backward compatibility, the field contains a fake sender user in non-channel chats, 
    if the message was sent on behalf of a chat.
    """
    sender_chat: Optional[Chat] = None
    """
    *Optional*. Sender of the message, sent on behalf of a chat. For example, 
    the channel itself for channel posts, 
    the supergroup itself for messages from anonymous group administrators, 
    the linked channel for messages automatically forwarded to the discussion group. 
    For backward compatibility, the field *from* contains a fake sender user in non-channel chats, 
    if the message was sent on behalf of a chat.
    """
    sender_boost_count: Optional[int] = None
    """
    *Optional*. If the sender of the message boosted the chat, the number of boosts added by the user
    """
    sender_business_bot: Optional[User] = None
    """
    *Optional*. The bot that actually sent the message on behalf of the business account. 
    Available only for outgoing messages sent on behalf of the connected business account.
    """
    business_connection_id: Optional[str] = None
    """
    *Optional*. Unique identifier of the business connection from which the message was received. 
    If non-empty, 
    the message belongs to a chat of the corresponding business account that is independent from any 
    potential bot chat which might share the same identifier.
    """
    forward_origin: Optional[MessageOrigin] = None
    """
    *Optional*. Information about the original message for forwarded messages
    """
    is_topic_message: Optional[bool] = None
    """
    *Optional*. *True*, if the message is sent to a forum topic
    """
    is_automatic_forward: Optional[bool] = None
    """
    *Optional*. *True*, 
    if the message is a channel post that was automatically forwarded to the connected discussion group
    """
    reply_to_message: Optional["Message"] = None
    """
    *Optional*. For replies in the same chat and message thread, the original message. 
    Note that the Message object in this field will not contain further *reply_to_message* fields even 
    if it itself is a reply.
    """
    external_reply: Optional[ExternalReplyInfo] = None
    """
    *Optional*. Information about the message that is being replied to, 
    which may come from another chat or forum topic
    """
    quote: Optional[TextQuote] = None
    """
    *Optional*. For replies that quote part of the original message, the quoted part of the message
    """
    reply_to_story: Optional[Story] = None
    """
    *Optional*. For replies to a story, the original story
    """
    via_bot: Optional[User] = None
    """
    *Optional*. Bot through which the message was sent
    """
    edit_date: Optional[int] = None
    """
    *Optional*. Date the message was last edited in Unix time
    """
    has_protected_content: Optional[bool] = None
    """
    *Optional*. *True*, if the message can't be forwarded
    """
    is_from_offline: Optional[bool] = None
    """
    *Optional*. True, if the message was sent by an implicit action, for example, 
    as an away or a greeting business message, or as a scheduled message
    """
    media_group_id: Optional[str] = None
    """
    *Optional*. The unique identifier of a media message group this message belongs to
    """
    author_signature: Optional[str] = None
    """
    *Optional*. Signature of the post author for messages in channels, 
    or the custom title of an anonymous group administrator
    """
    text: Optional[str] = None
    """
    *Optional*. For text messages, the actual UTF-8 text of the message
    """
    entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. 
    that appear in the text
    """
    link_preview_options: Optional[LinkPreviewOptions] = None
    """
    *Optional*. Options used for link preview generation for the message, 
    if it is a text message and link preview options were changed
    """
    animation: Optional[Animation] = None
    """
    *Optional*. Message is an animation, information about the animation. For backward compatibility, 
    when this field is set, the *document* field will also be set
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
    caption: Optional[str] = None
    """
    *Optional*. Caption for the animation, audio, document, photo, video or voice
    """
    caption_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, 
    etc. that appear in the caption
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
    poll: Optional[Poll] = None
    """
    *Optional*. Message is a native poll, information about the poll
    """
    venue: Optional[Venue] = None
    """
    *Optional*. Message is a venue, information about the venue. For backward compatibility, 
    when this field is set, the *location* field will also be set
    """
    location: Optional[Location] = None
    """
    *Optional*. Message is a shared location, information about the location
    """
    new_chat_members: Optional[list[User]] = None
    """
    *Optional*. 
    New members that were added to the group or supergroup and information about them (the bot itself 
    may be one of these members)
    """
    left_chat_member: Optional[User] = None
    """
    *Optional*. A member was removed from the group, 
    information about them (this member may be the bot itself)
    """
    new_chat_title: Optional[str] = None
    """
    *Optional*. A chat title was changed to this value
    """
    new_chat_photo: Optional[list[PhotoSize]] = None
    """
    *Optional*. A chat photo was change to this value
    """
    delete_chat_photo: Optional[bool] = None
    """
    *Optional*. Service message: the chat photo was deleted
    """
    group_chat_created: Optional[bool] = None
    """
    *Optional*. Service message: the group has been created
    """
    supergroup_chat_created: Optional[bool] = None
    """
    *Optional*. Service message: the supergroup has been created. 
    This field can't be received in a message coming through updates, 
    because bot can't be a member of a supergroup when it is created. 
    It can only be found in reply_to_message if someone replies to a very first message in a directly 
    created supergroup.
    """
    channel_chat_created: Optional[bool] = None
    """
    *Optional*. Service message: the channel has been created. 
    This field can't be received in a message coming through updates, 
    because bot can't be a member of a channel when it is created. 
    It can only be found in reply_to_message if someone replies to a very first message in a channel.
    """
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None
    """
    *Optional*. Service message: auto-delete timer settings changed in the chat
    """
    migrate_to_chat_id: Optional[int] = None
    """
    *Optional*. The group has been migrated to a supergroup with the specified identifier. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """
    migrate_from_chat_id: Optional[int] = None
    """
    *Optional*. The supergroup has been migrated from a group with the specified identifier. 
    This number may have more than 32 significant bits and some programming languages may have 
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits, 
    so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """
    pinned_message: Optional[Union["Message", InaccessibleMessage]] = None
    """
    *Optional*. Specified message was pinned. 
    Note that the Message object in this field will not contain further *reply_to_message* fields even 
    if it itself is a reply.
    """
    invoice: Optional[Invoice] = None
    """
    *Optional*. Message is an invoice for a `payment <https://core.telegram.org/bots/api#payments>`_, 
    information about the invoice. 
    `More about payments » <https://core.telegram.org/bots/api#payments>`_
    """
    successful_payment: Optional[SuccessfulPayment] = None
    """
    *Optional*. Message is a service message about a successful payment, 
    information about the payment. 
    `More about payments » <https://core.telegram.org/bots/api#payments>`_
    """
    users_shared: Optional[UsersShared] = None
    """
    *Optional*. Service message: users were shared with the bot
    """
    chat_shared: Optional[ChatShared] = None
    """
    *Optional*. Service message: a chat was shared with the bot
    """
    connected_website: Optional[str] = None
    """
    *Optional*. The domain name of the website on which the user has logged in. 
    `More about Telegram Login » <https://core.telegram.org/widgets/login>`_
    """
    write_access_allowed: Optional[WriteAccessAllowed] = None
    """
    *Optional*. 
    Service message: the user allowed the bot to write messages after adding it to the attachment or 
    side menu, launching a Web App from a link, 
    or accepting an explicit request from a Web App sent by the method `requestWriteAccess 
    <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_
    """
    passport_data: Optional[PassportData] = None
    """
    *Optional*. Telegram Passport data
    """
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    """
    *Optional*. Service message. 
    A user in the chat triggered another user's proximity alert while sharing Live Location.
    """
    boost_added: Optional[ChatBoostAdded] = None
    """
    *Optional*. Service message: user boosted the chat
    """
    forum_topic_created: Optional[ForumTopicCreated] = None
    """
    *Optional*. Service message: forum topic created
    """
    forum_topic_edited: Optional[ForumTopicEdited] = None
    """
    *Optional*. Service message: forum topic edited
    """
    forum_topic_closed: Optional[ForumTopicClosed] = None
    """
    *Optional*. Service message: forum topic closed
    """
    forum_topic_reopened: Optional[ForumTopicReopened] = None
    """
    *Optional*. Service message: forum topic reopened
    """
    general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None
    """
    *Optional*. Service message: the 'General' forum topic hidden
    """
    general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = None
    """
    *Optional*. Service message: the 'General' forum topic unhidden
    """
    giveaway_created: Optional[GiveawayCreated] = None
    """
    *Optional*. Service message: a scheduled giveaway was created
    """
    giveaway: Optional[Giveaway] = None
    """
    *Optional*. The message is a scheduled giveaway message
    """
    giveaway_winners: Optional[GiveawayWinners] = None
    """
    *Optional*. A giveaway with public winners was completed
    """
    giveaway_completed: Optional[GiveawayCompleted] = None
    """
    *Optional*. Service message: a giveaway without public winners was completed
    """
    video_chat_scheduled: Optional[VideoChatScheduled] = None
    """
    *Optional*. Service message: video chat scheduled
    """
    video_chat_started: Optional[VideoChatStarted] = None
    """
    *Optional*. Service message: video chat started
    """
    video_chat_ended: Optional[VideoChatEnded] = None
    """
    *Optional*. Service message: video chat ended
    """
    video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None
    """
    *Optional*. Service message: new participants invited to a video chat
    """
    web_app_data: Optional[WebAppData] = None
    """
    *Optional*. Service message: data sent by a Web App
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. Inline keyboard attached to the message. 
    :code:`login_url` buttons are represented as ordinary :code:`url` buttons.
    """
