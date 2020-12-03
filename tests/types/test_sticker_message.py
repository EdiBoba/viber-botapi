import pytest

from viber_botapi.types import StickerMessage


def test_sticker_message_serialize():
    data = {
        'tracking_data': 'tracking data',
        'sticker_id': 46105
    }
    obj = StickerMessage(**data)

    with pytest.raises(TypeError):
        obj.sticker_id = 'not int'

    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'sticker',
        'sticker_id': 46105
    }
    assert obj.serialize(add_min_api_ver=True) == expected
