import pytest

from viber_botapi.types import TextMessage


def test_text_message():
    data = {
        'tracking_data': 'tracking data',
        'text': 'Hello world!'
    }
    obj = TextMessage(**data)
    with pytest.raises(TypeError):
        obj.text = 123
    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'text',
        'text': 'Hello world!'
    }
    assert obj.serialize(add_min_api_ver=True) == expected
