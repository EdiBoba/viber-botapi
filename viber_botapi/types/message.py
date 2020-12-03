from abc import abstractmethod

from botapi import Field

from .base import ViberModel
from .keyboard import Keyboard


class Message(ViberModel):
    """Represents a Viber message object with general message parameters

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#general-send-message-parameters
    """

    tracking_data = Field()
    keyboard = Field(base=Keyboard)

    @property
    @abstractmethod
    def message_type(self):
        raise NotImplementedError
