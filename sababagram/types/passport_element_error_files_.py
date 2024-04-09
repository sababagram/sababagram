from dataclasses import dataclass, field

from .passport_element_error_ import PassportElementError


@dataclass
class PassportElementErrorFiles(PassportElementError):
    """
    Represents an issue with a list of scans.
    The error is considered resolved when the list of files containing the scans changes.

    Source: https://core.telegram.org/bots/api#passportelementerrorfiles
    """

    source: str = field(default="files", init=False)
    """
    Error source, must be *files*
    """
    type: str
    """
    The section of the user's Telegram Passport which has the issue, one of “utility_bill”, 
    “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    """
    file_hashes: list[str]
    """
    List of base64-encoded file hashes
    """
    message: str
    """
    Error message
    """
