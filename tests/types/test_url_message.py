import pytest

from viber_botapi.types import UrlMessage


def test_url_message():
    data = {
        'tracking_data': 'tracking data',
        'media': 'http://www.website.com/go_here'
    }
    obj = UrlMessage(**data)
    with pytest.raises(TypeError):
        obj.media = 123
    expected = {
        'type': 'url',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'media': 'http://www.website.com/go_here'
    }
    assert obj.serialize(add_min_api_ver=True) == expected
