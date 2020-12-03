from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class FileMessage(Message):
    """Represents a Viber file message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#file-message
    """

    message_type = Field(default='file', alias='type')
    media = Field(base=str)
    size = Field(base=int)
    file_name = Field(base=str)

    def __init__(
        self,
        media: str,
        size: int,
        file_name: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            media=media,
            size=size,
            file_name=file_name,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
