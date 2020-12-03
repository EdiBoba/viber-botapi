from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class StickerMessage(Message):
    """Represents a Viber sticker message object

    https://developers.viber.com/docs/api/rest-bot-api/#sticker-message
    """

    message_type = Field(default='sticker', alias='type')
    sticker_id = Field(base=int)

    def __init__(
        self,
        sticker_id: int,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            sticker_id=sticker_id,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
