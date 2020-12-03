import pytest

from viber_botapi.types import Sender


def test_sender_serialize():
    expected = {
        'name': 'John McClane',
        'avatar': 'http://avatar.example.com'
    }
    obj = Sender(**expected)

    with pytest.raises(TypeError):
        obj.name = 123

    with pytest.raises(TypeError):
        obj.avatar = 123

    assert obj.serialize() == expected
