from botapi import Field

from .base import ViberModel


class Contact(ViberModel):
    """Represents a Viber contact object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#contact-message
    """

    name = Field(base=str)
    phone_number = Field(base=str)

    def __init__(
        self,
        name: str,
        phone_number: str,
        **kwargs
    ):
        super().__init__(
            name=name,
            phone_number=phone_number,
            **kwargs
        )
