from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class EncryptedCredentials(BaseTelegramType):
    """
    Describes data required for decrypting and authenticating
    :class:`sababagram.types.EncryptedPassportElement`.
    See the `Telegram Passport Documentation
    <https://core.telegram.org/passport#receiving-information>`_ for a complete description of the
    data decryption and authentication processes.

    Source: https://core.telegram.org/bots/api#encryptedcredentials
    """

    data: str
    """
    Base64-encoded encrypted JSON-serialized data with unique user's payload, 
    data hashes and secrets required for :class:`sababagram.types.EncryptedPassportElement` decryption 
    and authentication
    """
    hash: str
    """
    Base64-encoded data hash for data authentication
    """
    secret: str
    """
    Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    """
