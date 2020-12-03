from typing import Optional, Union

from botapi import Field

from .keyboard import Keyboard
from .message import Message
from .rich_media import RichMedia


class RichMediaMessage(Message):
    """Represents a Viber rich media message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#rich-media-message--carousel-content-message
    """

    @property
    def min_api_version(self) -> int:
        return 7

    message_type = Field(default='rich_media', alias='type')
    rich_media = Field(base=RichMedia)
    alt_text = Field(base=str)

    def __init__(
        self,
        rich_media: Union[RichMedia, dict],
        alt_text: str = None,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            rich_media=rich_media,
            alt_text=alt_text,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
