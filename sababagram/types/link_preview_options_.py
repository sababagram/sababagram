from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType


@dataclass
class LinkPreviewOptions(BaseTelegramType):
    """
    Describes the options used for link preview generation.

    Source: https://core.telegram.org/bots/api#linkpreviewoptions
    """

    is_disabled: Optional[bool] = None
    """
    *Optional*. *True*, if the link preview is disabled
    """
    url: Optional[str] = None
    """
    *Optional*. URL to use for the link preview. If empty, 
    then the first URL found in the message text will be used
    """
    prefer_small_media: Optional[bool] = None
    """
    *Optional*. *True*, if the media in the link preview is supposed to be shrunk; 
    ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    """
    prefer_large_media: Optional[bool] = None
    """
    *Optional*. *True*, if the media in the link preview is supposed to be enlarged; 
    ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    """
    show_above_text: Optional[bool] = None
    """
    *Optional*. *True*, if the link preview must be shown above the message text; otherwise, 
    the link preview will be shown below the message text
    """
