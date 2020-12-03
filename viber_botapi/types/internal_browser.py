from botapi import Field

from .base import ViberModel


class InternalBrowser(ViberModel):
    """Represents a Viber internal browser object

    Params:
    https://developers.viber.com/docs/tools/keyboards/#buttons-parameters
    """

    @property
    def min_api_version(self) -> int:
        return 3 if self.action_reply_data is None else 6

    action_button = Field(base=str, alias='ActionButton')
    action_predefined_url = Field(base=str, alias='ActionPredefinedURL')
    title_type = Field(base=str, alias='TitleType')
    custom_title = Field(base=str, alias='CustomTitle')
    mode = Field(base=str, alias='Mode')
    footer_type = Field(base=str, alias='FooterType')
    action_reply_data = Field(base=str, alias='ActionReplyData')

    def __init__(
        self,
        action_button: str = None,
        action_predefined_url: str = None,
        title_type: str = None,
        custom_title: str = None,
        mode: str = None,
        footer_type: str = None,
        action_reply_data: str = None,
        **kwargs
    ):
        super().__init__(
            action_button=action_button,
            action_predefined_url=action_predefined_url,
            title_type=title_type,
            custom_title=custom_title,
            mode=mode,
            footer_type=footer_type,
            action_reply_data=action_reply_data,
            **kwargs
        )
