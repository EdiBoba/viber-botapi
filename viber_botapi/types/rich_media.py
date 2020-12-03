from typing import Optional, Union

from botapi import ListField, Field

from .base import ViberModel
from .button import Button
from .favorites_metadata import FavoritesMetadata


class RichMedia(ViberModel):
    """Represents a Viber rich media object

    Params:
    https://developers.viber.com/docs/api/rest-bot-api/#rich-media-message--carousel-content-message

    Keyboards:
    https://developers.viber.com/docs/tools/keyboards/

    Keyboards examples:
    https://developers.viber.com/docs/tools/keyboard-examples/

    Favorites metadata:
    https://developers.viber.com/docs/tools/keyboards/#favoritesMetadata
    """

    buttons = ListField(item_base=Button, default=[], alias='Buttons')
    bg_color = Field(base=str, alias='BgColor')
    media_type = Field(default='rich_media', alias='Type')
    buttons_group_columns = Field(base=int, alias='ButtonsGroupColumns')
    buttons_group_rows = Field(base=int, alias='ButtonsGroupRows')
    favorites_metadata = Field(base=FavoritesMetadata, alias='FavoritesMetadata')

    def __init__(
        self,
        buttons: list = None,
        bg_color: str = None,
        buttons_group_columns: int = None,
        buttons_group_rows: int = None,
        favorites_metadata: Union[FavoritesMetadata, dict, None] = None,
        **kwargs
    ):
        super().__init__(
            buttons=buttons,
            bg_color=bg_color,
            buttons_group_columns=buttons_group_columns,
            buttons_group_rows=buttons_group_rows,
            favorites_metadata=favorites_metadata,
            **kwargs)
