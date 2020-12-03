import pytest

from viber_botapi.types import Message


def test_abstract_message():
    with pytest.raises(TypeError):
        Message()
