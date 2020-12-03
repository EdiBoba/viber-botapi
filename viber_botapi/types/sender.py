from typing import Optional

from botapi import Field

from .base import ViberModel


class Sender(ViberModel):
    """Represents a Viber sender object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#general-send-message-parameters
    """

    name = Field(base=str)
    avatar = Field(base=str)

    def __init__(
        self,
        name: Optional[str],
        avatar: Optional[str] = None,
        **kwargs
    ):
        super().__init__(
            name=name,
            avatar=avatar,
            **kwargs)
