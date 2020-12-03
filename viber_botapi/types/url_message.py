from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class UrlMessage(Message):
    """Represents a Viber url message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#url-message
    """

    message_type = Field(default='url', alias='type')
    media = Field(base=str)

    def __init__(
        self,
        media: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            media=media,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
