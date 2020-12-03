from botapi import Field

from .base import ViberModel


class FavoritesMetadata(ViberModel):
    """
    Represents a Viber favorites metadata object

    Params:
    https://developers.viber.com/docs/tools/keyboards/#favorites-metadata
    """

    data_type = Field(base=str, alias='type')
    url = Field(base=str)
    title = Field(base=str)
    thumbnail = Field(base=str)
    domain = Field(base=str)
    width = Field(base=int)
    height = Field(base=int)
    alternative_url = Field(base=str, alias='alternativeUrl')
    alternative_text = Field(base=str, alias='alternativeText')

    def __init__(
        self,
        data_type: str = None,
        url: str = None,
        title: str = None,
        thumbnail: str = None,
        domain: str = None,
        width: int = None,
        height: int = None,
        alternative_url: str = None,
        alternative_text: str = None,
        **kwargs
    ):
        super().__init__(
            data_type=data_type,
            url=url,
            title=title,
            thumbnail=thumbnail,
            domain=domain,
            width=width,
            height=height,
            alternative_url=alternative_url,
            alternative_text=alternative_text,
            **kwargs
        )
