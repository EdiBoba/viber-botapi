from typing import Optional

from botapi import Field

from .keyboard import Keyboard
from .location import Location
from .message import Message


class LocationMessage(Message):
    """Represents a Viber location message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#location-message
    """

    message_type = Field(default='location', alias='type')
    location = Field(base=Location)

    def __init__(
        self,
        location: Location,
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.location = location
        self.tracking_data = tracking_data
        self.keyboard = keyboard
