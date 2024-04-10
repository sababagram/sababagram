from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class InlineQueryResult(BaseTelegramType):
    """
    This object represents one result of an inline query.
    Telegram clients currently support results of the following 20 types: -
    :class:`sababagram.types.InlineQueryResultCachedAudio` -
    :class:`sababagram.types.InlineQueryResultCachedDocument` -
    :class:`sababagram.types.InlineQueryResultCachedGif` -
    :class:`sababagram.types.InlineQueryResultCachedMpeg4Gif` -
    :class:`sababagram.types.InlineQueryResultCachedPhoto` -
    :class:`sababagram.types.InlineQueryResultCachedSticker` -
    :class:`sababagram.types.InlineQueryResultCachedVideo` -
    :class:`sababagram.types.InlineQueryResultCachedVoice` -
    :class:`sababagram.types.InlineQueryResultArticle` -
    :class:`sababagram.types.InlineQueryResultAudio` -
    :class:`sababagram.types.InlineQueryResultContact` -
    :class:`sababagram.types.InlineQueryResultGame` -
    :class:`sababagram.types.InlineQueryResultDocument` -
    :class:`sababagram.types.InlineQueryResultGif` -
    :class:`sababagram.types.InlineQueryResultLocation` -
    :class:`sababagram.types.InlineQueryResultMpeg4Gif` -
    :class:`sababagram.types.InlineQueryResultPhoto` -
    :class:`sababagram.types.InlineQueryResultVenue` -
    :class:`sababagram.types.InlineQueryResultVideo` -
    :class:`sababagram.types.InlineQueryResultVoice`**Note:** All URLs passed in inline query results
    will be available to end users and therefore must be assumed to be **public**.

    Source: https://core.telegram.org/bots/api#inlinequeryresult
    """
