from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class PictureMessage(Message):
    """Represents a Viber picture message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#picture-message
    """

    message_type = Field(default='picture', alias='type')
    text = Field(base=str)
    media = Field(base=str)
    thumbnail = Field(base=str)

    def __init__(
        self,
        text: str,
        media: str,
        thumbnail: Optional[str] = None,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            text=text,
            media=media,
            thumbnail=thumbnail,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
