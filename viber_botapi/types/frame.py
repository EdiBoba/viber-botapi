from botapi import Field

from .base import ViberModel


class Frame(ViberModel):
    """Represents a Viber frame object

    Params:
    https://developers.viber.com/docs/tools/keyboards/#buttons-parameters
    """

    @property
    def min_api_version(self) -> int:
        return 6

    border_width = Field(base=int, alias='BorderWidth')
    border_color = Field(base=str, alias='BorderColor')
    corner_radius = Field(base=int, alias='CornerRadius')

    def __init__(
        self,
        border_width: int = None,
        border_color: str = None,
        corner_radius: int = None,
        **kwargs
    ):
        super().__init__(
            border_width=border_width,
            border_color=border_color,
            corner_radius=corner_radius,
            **kwargs
        )
