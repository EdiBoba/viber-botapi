import pytest

from viber_botapi.types import Webhook


def test_webhook():
    expected = {
        'url': 'https://my.host.com',
        'event_types': [
            'delivered',
            'seen',
            'failed',
            'subscribed',
            'unsubscribed',
            'conversation_started'
        ],
        'send_name': True,
        'send_photo': True
    }

    obj = Webhook(**expected)

    obj.event_types.pop(-1)
    obj.event_types.append('conversation_started')

    with pytest.raises(TypeError):
        obj.event_types.append(123)

    with pytest.raises(TypeError):
        obj.event_types = 123

    with pytest.raises(TypeError):
        obj.send_name = 'not bool'

    with pytest.raises(TypeError):
        obj.send_photo = 'not bool'

    with pytest.raises(TypeError):
        obj.url = 123

    assert obj.serialize() == expected
