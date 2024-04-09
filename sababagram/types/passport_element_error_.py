from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class PassportElementError(BaseTelegramType):
    """
    This object represents an error in the Telegram Passport element which was submitted that should
    be resolved by the user.
    It should be one of: - :class:`sababagram.types.PassportElementErrorDataField` -
    :class:`sababagram.types.PassportElementErrorFrontSide` -
    :class:`sababagram.types.PassportElementErrorReverseSide` -
    :class:`sababagram.types.PassportElementErrorSelfie` -
    :class:`sababagram.types.PassportElementErrorFile` -
    :class:`sababagram.types.PassportElementErrorFiles` -
    :class:`sababagram.types.PassportElementErrorTranslationFile` -
    :class:`sababagram.types.PassportElementErrorTranslationFiles` -
    :class:`sababagram.types.PassportElementErrorUnspecified`

    Source: https://core.telegram.org/bots/api#passportelementerror
    """
