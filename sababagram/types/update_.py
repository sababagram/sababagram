from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .business_connection_ import BusinessConnection
from .business_messages_deleted_ import BusinessMessagesDeleted
from .callback_query_ import CallbackQuery
from .chat_boost_removed_ import ChatBoostRemoved
from .chat_boost_updated_ import ChatBoostUpdated
from .chat_join_request_ import ChatJoinRequest
from .chat_member_updated_ import ChatMemberUpdated
from .chosen_inline_result_ import ChosenInlineResult
from .inline_query_ import InlineQuery
from .message_ import Message
from .message_reaction_count_updated_ import MessageReactionCountUpdated
from .message_reaction_updated_ import MessageReactionUpdated
from .poll_ import Poll
from .poll_answer_ import PollAnswer
from .pre_checkout_query_ import PreCheckoutQuery
from .shipping_query_ import ShippingQuery


@dataclass
class Update(BaseTelegramType):
    """
    This `object <https://core.telegram.org/bots/api#available-types>`_ represents an incoming update.
    At most **one** of the optional parameters can be present in any given update.

    Source: https://core.telegram.org/bots/api#update
    """

    update_id: int
    """
    The update's unique identifier. 
    Update identifiers start from a certain positive number and increase sequentially. 
    This identifier becomes especially handy if you're using `webhooks 
    <https://core.telegram.org/bots/api#setwebhook>`_, 
    since it allows you to ignore repeated updates or to restore the correct update sequence, 
    should they get out of order. If there are no new updates for at least a week, 
    then identifier of the next update will be chosen randomly instead of sequentially.
    """
    message: Optional[Message] = None
    """
    *Optional*. New incoming message of any kind - text, photo, sticker, etc.
    """
    edited_message: Optional[Message] = None
    """
    *Optional*. New version of a message that is known to the bot and was edited. 
    This update may at times be triggered by changes to message fields that are either unavailable or 
    not actively used by your bot.
    """
    channel_post: Optional[Message] = None
    """
    *Optional*. New incoming channel post of any kind - text, photo, sticker, etc.
    """
    edited_channel_post: Optional[Message] = None
    """
    *Optional*. New version of a channel post that is known to the bot and was edited. 
    This update may at times be triggered by changes to message fields that are either unavailable or 
    not actively used by your bot.
    """
    business_connection: Optional[BusinessConnection] = None
    """
    *Optional*. The bot was connected to or disconnected from a business account, 
    or a user edited an existing connection with the bot
    """
    business_message: Optional[Message] = None
    """
    *Optional*. New non-service message from a connected business account
    """
    edited_business_message: Optional[Message] = None
    """
    *Optional*. New version of a message from a connected business account
    """
    deleted_business_messages: Optional[BusinessMessagesDeleted] = None
    """
    *Optional*. Messages were deleted from a connected business account
    """
    message_reaction: Optional[MessageReactionUpdated] = None
    """
    *Optional*. A reaction to a message was changed by a user. 
    The bot must be an administrator in the chat and must explicitly specify 
    :code:`"message_reaction"` in the list of *allowed_updates* to receive these updates. 
    The update isn't received for reactions set by bots.
    """
    message_reaction_count: Optional[MessageReactionCountUpdated] = None
    """
    *Optional*. Reactions to a message with anonymous reactions were changed. 
    The bot must be an administrator in the chat and must explicitly specify 
    :code:`"message_reaction_count"` in the list of *allowed_updates* to receive these updates. 
    The updates are grouped and can be sent with delay up to a few minutes.
    """
    inline_query: Optional[InlineQuery] = None
    """
    *Optional*. New incoming `inline <https://core.telegram.org/bots/api#inline-mode>`_ query
    """
    chosen_inline_result: Optional[ChosenInlineResult] = None
    """
    *Optional*. 
    The result of an `inline <https://core.telegram.org/bots/api#inline-mode>`_ query that was chosen 
    by a user and sent to their chat partner. 
    Please see our documentation on the `feedback collecting 
    <https://core.telegram.org/bots/inline#collecting-feedback>`_ for details on how to enable these 
    updates for your bot.
    """
    callback_query: Optional[CallbackQuery] = None
    """
    *Optional*. New incoming callback query
    """
    shipping_query: Optional[ShippingQuery] = None
    """
    *Optional*. New incoming shipping query. Only for invoices with flexible price
    """
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    """
    *Optional*. New incoming pre-checkout query. Contains full information about checkout
    """
    poll: Optional[Poll] = None
    """
    *Optional*. New poll state. Bots receive only updates about manually stopped polls and polls, 
    which are sent by the bot
    """
    poll_answer: Optional[PollAnswer] = None
    """
    *Optional*. A user changed their answer in a non-anonymous poll. 
    Bots receive new votes only in polls that were sent by the bot itself.
    """
    my_chat_member: Optional[ChatMemberUpdated] = None
    """
    *Optional*. The bot's chat member status was updated in a chat. For private chats, 
    this update is received only when the bot is blocked or unblocked by the user.
    """
    chat_member: Optional[ChatMemberUpdated] = None
    """
    *Optional*. A chat member's status was updated in a chat. 
    The bot must be an administrator in the chat and must explicitly specify :code:`"chat_member"` in 
    the list of *allowed_updates* to receive these updates.
    """
    chat_join_request: Optional[ChatJoinRequest] = None
    """
    *Optional*. A request to join the chat has been sent. 
    The bot must have the *can_invite_users* administrator right in the chat to receive these updates.
    """
    chat_boost: Optional[ChatBoostUpdated] = None
    """
    *Optional*. A chat boost was added or changed. 
    The bot must be an administrator in the chat to receive these updates.
    """
    removed_chat_boost: Optional[ChatBoostRemoved] = None
    """
    *Optional*. A boost was removed from a chat. 
    The bot must be an administrator in the chat to receive these updates.
    """
