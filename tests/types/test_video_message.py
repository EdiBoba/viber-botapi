import pytest

from viber_botapi.types import VideoMessage


def test_video_message():
    expected = {
        'type': 'video',
        'min_api_version': 1,
        'media': 'http://www.images.com/video.mp4',
        'size': 10000,
        'thumbnail': 'http://www.images.com/thumb.jpg',
        'duration': 10,
        'tracking_data': 'tracking data'
    }

    obj = VideoMessage(**expected)

    with pytest.raises(TypeError):
        obj.media = 123

    with pytest.raises(TypeError):
        obj.size = 'not int'

    with pytest.raises(TypeError):
        obj.thumbnail = 123

    with pytest.raises(TypeError):
        obj.duration = 'not int'

    assert obj.serialize(add_min_api_ver=True) == expected
