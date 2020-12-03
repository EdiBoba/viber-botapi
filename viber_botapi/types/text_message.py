from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .message import Message


class TextMessage(Message):
    """Represents a Viber text message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#text-message
    """

    message_type = Field(default='text', alias='type')
    text = Field(base=str)

    def __init__(
        self,
        text: str,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            text=text,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
