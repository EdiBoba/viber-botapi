from typing import Union

from botapi import Field, ListField

from .base import ViberModel
from .button import Button
from .favorites_metadata import FavoritesMetadata


class Keyboard(ViberModel):
    """Represents a Viber keyboard object

    Keyboards:
    https://developers.viber.com/docs/tools/keyboards/

    Keyboards examples:
    https://developers.viber.com/docs/tools/keyboard-examples/
    """

    @property
    def min_api_version(self) -> int:
        if self.favorites_metadata is not None:
            return 6
        elif self.buttons_group_columns is not None or \
                self.buttons_group_rows is not None or \
                self.input_field_state is not None:
            return 4
        elif self.custom_default_height is not None or self.height_scale is not None:
            return 3
        else:
            return 1

    kb_type = Field(default='keyboard', alias='Type')
    buttons = ListField(item_base=Button, default=[], alias='Buttons')
    bg_color = Field(base=str, alias='BgColor')
    default_height = Field(base=bool, alias='DefaultHeight')
    custom_default_height = Field(base=int, alias='CustomDefaultHeight')
    height_scale = Field(base=int, alias='HeightScale')
    buttons_group_columns = Field(base=int, alias='ButtonsGroupColumns')
    buttons_group_rows = Field(base=int, alias='ButtonsGroupRows')
    input_field_state = Field(base=str, alias='InputFieldState')
    favorites_metadata = Field(base=FavoritesMetadata, alias='FavoritesMetadata')

    def __init__(
        self,
        buttons: list = None,
        bg_color: str = None,
        default_height: bool = None,
        custom_default_height: int = None,
        height_scale: int = None,
        buttons_group_columns: int = None,
        buttons_group_rows: int = None,
        input_field_state: str = None,
        favorites_metadata: Union[FavoritesMetadata, dict, None] = None,
        **kwargs
    ):
        super().__init__(
            buttons=buttons,
            bg_color=bg_color,
            default_height=default_height,
            custom_default_height=custom_default_height,
            height_scale=height_scale,
            buttons_group_columns=buttons_group_columns,
            buttons_group_rows=buttons_group_rows,
            input_field_state=input_field_state,
            favorites_metadata=favorites_metadata,
            **kwargs
        )
