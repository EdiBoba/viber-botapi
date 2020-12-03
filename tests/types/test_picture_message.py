import pytest

from viber_botapi.types import PictureMessage


def test_pic_message_serialize():
    data = {
        'tracking_data': 'tracking data',
        'text': 'Photo description',
        'media': 'http://www.images.com/img.jpg',
        'thumbnail': 'http://www.images.com/thumb.jpg'
    }
    obj = PictureMessage(**data)

    with pytest.raises(TypeError):
        obj.text = 123

    with pytest.raises(TypeError):
        obj.media = 123

    with pytest.raises(TypeError):
        obj.thumbnail = 123

    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'picture',
        'text': 'Photo description',
        'media': 'http://www.images.com/img.jpg',
        'thumbnail': 'http://www.images.com/thumb.jpg'
    }
    assert obj.serialize(add_min_api_ver=True) == expected
