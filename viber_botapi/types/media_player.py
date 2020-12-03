from botapi import Field

from .base import ViberModel


class MediaPlayer(ViberModel):
    """Represents a Viber media player object

    Params:
    https://developers.viber.com/docs/tools/keyboards/#buttons-parameters
    """

    @property
    def min_api_version(self) -> int:
        return 6

    title = Field(base=str, alias='Title')
    subtitle = Field(base=str, alias='Subtitle')
    thumbnail_url = Field(base=str, alias='ThumbnailURL')
    loop = Field(base=bool, alias='Loop')

    def __init__(
        self,
        title: str = None,
        subtitle: str = None,
        thumbnail_url: str = None,
        loop: bool = None,
        **kwargs
    ):
        super().__init__(
            title=title,
            subtitle=subtitle,
            thumbnail_url=thumbnail_url,
            loop=loop,
            **kwargs
        )
