from typing import Optional, Union

from botapi import Field

from .contact import Contact
from .keyboard import Keyboard
from .message import Message


class ContactMessage(Message):
    """Represents a Viber contact message object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#contact-message
    """

    message_type = Field(default='contact', alias='type')
    contact = Field(base=Contact)

    def __init__(
        self,
        contact: Union[Contact, dict],
        tracking_data: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
        **kwargs
    ):
        super().__init__(
            contact=contact,
            tracking_data=tracking_data,
            keyboard=keyboard,
            **kwargs
        )
