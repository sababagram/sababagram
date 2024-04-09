from dataclasses import dataclass

from .base import BaseTelegramType
from .encrypted_credentials_ import EncryptedCredentials
from .encrypted_passport_element_ import EncryptedPassportElement


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
