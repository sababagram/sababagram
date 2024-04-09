from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup_ import InlineKeyboardMarkup
from .inline_query_result_ import InlineQueryResult
from .input_message_content_ import InputMessageContent


@dataclass
class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.

    Source: https://core.telegram.org/bots/api#inlinequeryresultarticle
    """

    type: str = field(default="article", init=False)
    """
    Type of the result, must be *article*
    """
    id: str
    """
    Unique identifier for this result, 1-64 Bytes
    """
    title: str
    """
    Title of the result
    """
    input_message_content: InputMessageContent
    """
    Content of the message to be sent
    """
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """
    *Optional*. 
    `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the 
    message
    """
    url: Optional[str] = None
    """
    *Optional*. URL of the result
    """
    hide_url: Optional[bool] = None
    """
    *Optional*. Pass *True* if you don't want the URL to be shown in the message
    """
    description: Optional[str] = None
    """
    *Optional*. Short description of the result
    """
    thumbnail_url: Optional[str] = None
    """
    *Optional*. Url of the thumbnail for the result
    """
    thumbnail_width: Optional[int] = None
    """
    *Optional*. Thumbnail width
    """
    thumbnail_height: Optional[int] = None
    """
    *Optional*. Thumbnail height
    """
