from viber_botapi.types import Button, InternalBrowser, Map, Frame, MediaPlayer


def test_button():
    expected = {
        'ActionBody': 'action body',
        'Columns': 6,
        'Rows': 1,
        'BgColor': '#000000',
        'Silent': True,
        'BgMediaType': 'picture',
        'BgMedia': 'some_url',
        'BgMediaScaleType': 'crop',
        'ImageScaleType': 'crop',
        'BgLoop': True,
        'ActionType': 'reply',
        'Image': 'some_url',
        'Text': 'text',
        'TextVAlign': 'middle',
        'TextHAlign': 'center',
        'TextPaddings': [12, 12, 12, 12],
        'TextOpacity': 100,
        'TextSize': 'regular',
        'OpenURLType': 'internal',
        'OpenURLMediaType': 'not-media',
        'TextBgGradientColor': '#000000',
        'TextShouldFit': False,
        'InternalBrowser': {
            'ActionButton': 'forward',
            'ActionPredefinedURL': 'some_url',
            'TitleType': 'default',
            'CustomTitle': 'custom_title',
            'Mode': 'fullscreen',
            'FooterType': 'default',
        },
        'Map': {
            'Latitude': '37.7898',
            'Longitude': '-122.3942',
        },
        'Frame': {
            'BorderWidth': 1,
            'BorderColor': '#000000',
            'CornerRadius': 0,
        },
        'MediaPlayer': {
            'Title': 'title',
            'Subtitle': 'subtitle',
            'ThumbnailURL': 'some_url',
            'Loop': False,
        }
    }

    obj = Button(**expected)
    assert type(obj.internal_browser) == InternalBrowser
    assert type(obj.open_map) == Map
    assert type(obj.frame) == Frame
    assert type(obj.media_player) == MediaPlayer
    assert obj.serialize() == expected
