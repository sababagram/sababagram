from dataclasses import dataclass
from typing import Optional

from . import PassportFile
from .base import BaseTelegramType


@dataclass
class EncryptedPassportElement(BaseTelegramType):
    """
    Describes documents or other Telegram Passport elements shared with the bot by the user.

    Source: https://core.telegram.org/bots/api#encryptedpassportelement
    """

    type: str
    """
    Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, 
    “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, 
    “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    """
    hash: str
    """
    Base64-encoded element hash for using in :class:`sababagram.types.PassportElementErrorUnspecified`
    """
    data: Optional[str] = None
    """
    *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user; 
    available only for “personal_details”, “passport”, “driver_license”, “identity_card”, 
    “internal_passport” and “address” types. 
    Can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
    phone_number: Optional[str] = None
    """
    *Optional*. User's verified phone number; available only for “phone_number” type
    """
    email: Optional[str] = None
    """
    *Optional*. User's verified email address; available only for “email” type
    """
    files: Optional[list[PassportFile]] = None
    """
    *Optional*. Array of encrypted files with documents provided by the user; 
    available only for “utility_bill”, “bank_statement”, “rental_agreement”, 
    “passport_registration” and “temporary_registration” types. 
    Files can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
    front_side: Optional[PassportFile] = None
    """
    *Optional*. Encrypted file with the front side of the document, provided by the user; 
    available only for “passport”, “driver_license”, “identity_card” and “internal_passport”. 
    The file can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
    reverse_side: Optional[PassportFile] = None
    """
    *Optional*. Encrypted file with the reverse side of the document, provided by the user; 
    available only for “driver_license” and “identity_card”. 
    The file can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
    selfie: Optional[PassportFile] = None
    """
    *Optional*. Encrypted file with the selfie of the user holding a document, provided by the user; 
    available if requested for “passport”, “driver_license”, “identity_card” and “internal_passport”. 
    The file can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
    translation: Optional[list[PassportFile]] = None
    """
    *Optional*. Array of encrypted files with translated versions of documents provided by the user; 
    available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, 
    “utility_bill”, “bank_statement”, “rental_agreement”, 
    “passport_registration” and “temporary_registration” types. 
    Files can be decrypted and verified using the accompanying 
    :class:`sababagram.types.EncryptedCredentials`.
    """
