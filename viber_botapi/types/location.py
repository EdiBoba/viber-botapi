from botapi import Field

from .base import ViberModel


class Location(ViberModel):
    """Represents a Viber location object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#location-message
    """

    latitude = Field(base=str, alias='lat')
    longitude = Field(base=str, alias='lon')

    def __init__(
        self,
        latitude: str = None,
        longitude: str = None,
        **kwargs
    ):
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            **kwargs
        )
