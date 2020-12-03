from typing import Union

from botapi import Field, ListField

from .base import ViberModel
from .frame import Frame
from .internal_browser import InternalBrowser
from .map import Map
from .media_player import MediaPlayer


class Button(ViberModel):
    """Represents a Viber button object

    Params:
    https://developers.viber.com/docs/tools/keyboard-examples/
    """

    @property
    def min_api_version(self) -> int:
        if self.bg_media_scale_type is not None or \
                self.image_scale_type is not None or \
                self.text_should_fit is not None:
            return 6
        elif self.text_paddings is not None:
            return 4
        else:
            return 1

    columns = Field(base=int, alias='Columns')
    rows = Field(base=int, alias='Rows')
    bg_color = Field(base=str, alias='BgColor')
    silent = Field(base=bool, alias='Silent')
    bg_media_type = Field(base=str, alias='BgMediaType')
    bg_media = Field(base=str, alias='BgMedia')
    bg_media_scale_type = Field(base=str, alias='BgMediaScaleType')
    image_scale_type = Field(base=str, alias='ImageScaleType')
    bg_loop = Field(base=bool, alias='BgLoop')
    action_type = Field(base=str, alias='ActionType')
    action_body = Field(base=str, alias='ActionBody')
    image = Field(base=str, alias='Image')
    text = Field(base=str, alias='Text')
    text_v_align = Field(base=str, alias='TextVAlign')
    text_h_align = Field(base=str, alias='TextHAlign')
    text_paddings = ListField(item_base=int, alias='TextPaddings')
    text_opacity = Field(base=int, alias='TextOpacity')
    text_size = Field(base=str, alias='TextSize')
    open_url_type = Field(base=str, alias='OpenURLType')
    open_url_media_type = Field(base=str, alias='OpenURLMediaType')
    text_bg_gradient_color = Field(base=str, alias='TextBgGradientColor')
    text_should_fit = Field(base=bool, alias='TextShouldFit')
    internal_browser = Field(base=InternalBrowser, alias='InternalBrowser')
    open_map = Field(base=Map, alias='Map')
    frame = Field(base=Frame, alias='Frame')
    media_player = Field(base=MediaPlayer, alias='MediaPlayer')

    def __init__(
        self,
        columns: int = None,
        rows: int = None,
        bg_color: str = None,
        silent: bool = None,
        bg_media_type: str = None,
        bg_media: str = None,
        bg_media_scale_type: str = None,
        image_scale_type: str = None,
        bg_loop: bool = None,
        action_type: str = None,
        action_body: str = None,
        image: str = None,
        text: str = None,
        text_v_align: str = None,
        text_h_align: str = None,
        text_paddings: list = None,
        text_opacity: int = None,
        text_size: str = None,
        open_url_type: str = None,
        open_url_media_type: str = None,
        text_bg_gradient_color: str = None,
        text_should_fit: bool = None,
        internal_browser: Union[InternalBrowser, dict, None] = None,
        open_map: Union[Map, dict, None] = None,
        frame: Union[Frame, dict, None] = None,
        media_player: Union[MediaPlayer, dict, None] = None,
        **kwargs
    ):
        super().__init__(
            columns=columns,
            rows=rows,
            bg_color=bg_color,
            silent=silent,
            bg_media_type=bg_media_type,
            bg_media=bg_media,
            bg_media_scale_type=bg_media_scale_type,
            image_scale_type=image_scale_type,
            bg_loop=bg_loop,
            action_type=action_type,
            action_body=action_body,
            image=image,
            text=text,
            text_v_align=text_v_align,
            text_h_align=text_h_align,
            text_paddings=text_paddings,
            text_opacity=text_opacity,
            text_size=text_size,
            open_url_type=open_url_type,
            open_url_media_type=open_url_media_type,
            text_bg_gradient_color=text_bg_gradient_color,
            text_should_fit=text_should_fit,
            internal_browser=internal_browser,
            open_map=open_map,
            frame=frame,
            media_player=media_player,
            **kwargs
        )
