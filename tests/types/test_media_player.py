from viber_botapi.types import MediaPlayer


def test_media_player_serialize():
    data = {
        'Title': 'title',
        'Subtitle': 'subtitle',
        'ThumbnailURL': 'some_url',
        'Loop': False,
    }

    obj = MediaPlayer(**data)

    expected = {
        'Title': 'title',
        'Subtitle': 'subtitle',
        'ThumbnailURL': 'some_url',
        'Loop': False,
        'min_api_version': 6
    }
    assert obj.serialize(add_min_api_ver=True) == expected
