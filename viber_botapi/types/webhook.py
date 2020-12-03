from typing import Optional

from botapi import Field, ListField

from .base import ViberModel


class Webhook(ViberModel):
    """Model for work with Viber webhook

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#resource-url

    Remove webhook:
    https://developers.viber.com/docs/api/rest-bot-api/#removing-your-webhook

    Response:
    https://developers.viber.com/docs/api/rest-bot-api/#set-webhook-response

    Event types:
    https://developers.viber.com/docs/api/rest-bot-api/#event-types-filtering
    """

    url = Field(base=str)
    event_types = ListField(item_base=str)
    send_name = Field(base=bool)
    send_photo = Field(base=bool)

    def __init__(
        self,
        url: str,
        event_types: Optional[list] = None,
        send_name: Optional[bool] = None,
        send_photo: Optional[bool] = None,
        **kwargs
    ):
        super().__init__(
            url=url,
            event_types=event_types,
            send_name=send_name,
            send_photo=send_photo,
            **kwargs
        )
