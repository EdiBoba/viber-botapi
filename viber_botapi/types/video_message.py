from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class VideoMessage(Message):
    """Represents a Viber video message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#video-message
    """

    message_type = Field(default='video', alias='type')
    media = Field(base=str)
    size = Field(base=int)
    duration = Field(base=int)
    thumbnail = Field(base=str)

    def __init__(
        self,
        media: str,
        size: int,
        duration: Optional[int] = None,
        thumbnail: Optional[str] = None,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            media=media,
            size=size,
            duration=duration,
            thumbnail=thumbnail,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
