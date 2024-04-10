from dataclasses import dataclass

from . import EncryptedCredentials, EncryptedPassportElement
from .base import BaseTelegramType


@dataclass
class PassportData(BaseTelegramType):
    """
    Describes Telegram Passport data shared with the bot by the user.

    Source: https://core.telegram.org/bots/api#passportdata
    """

    data: list[EncryptedPassportElement]
    """
    Array with information about documents and other Telegram Passport elements that was shared with 
    the bot
    """
    credentials: EncryptedCredentials
    """
    Encrypted credentials required to decrypt the data
    """
