from viber_botapi.types import InternalBrowser


def test_internal_browser():
    data = {
        'ActionButton': 'forward',
        'ActionPredefinedURL': 'some_url',
        'TitleType': 'default',
        'CustomTitle': 'custom_title',
        'Mode': 'fullscreen',
        'FooterType': 'default',
    }

    obj = InternalBrowser(**data)

    assert obj.min_api_version == 3

    obj.action_reply_data = 'action_reply'

    expected = {
        'ActionButton': 'forward',
        'ActionPredefinedURL': 'some_url',
        'TitleType': 'default',
        'CustomTitle': 'custom_title',
        'Mode': 'fullscreen',
        'FooterType': 'default',
        'ActionReplyData': 'action_reply',
        'min_api_version': 6
    }
    assert obj.serialize(add_min_api_ver=True) == expected
