from botapi import Field

from .base import ViberModel


class Map(ViberModel):
    """Represents a Viber map object

    Params:
    https://developers.viber.com/docs/tools/keyboards/#buttons-parameters
    """
    @property
    def min_api_version(self) -> int:
        return 6

    latitude = Field(alias='Latitude')
    longitude = Field(alias='Longitude')

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
