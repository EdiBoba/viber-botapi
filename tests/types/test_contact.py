import pytest

from viber_botapi.types import Contact


def test_contact():
    expected = {
        'name': 'Itamar',
        'phone_number': '+972511123123'
    }

    obj = Contact(**expected)

    with pytest.raises(TypeError):
        obj.name = 123

    with pytest.raises(TypeError):
        obj.phone_number = 123

    assert obj.serialize() == expected
