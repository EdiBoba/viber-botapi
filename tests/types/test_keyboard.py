from viber_botapi.types import Keyboard, Button


def test_keyboard():
    expected = {
        'Type': 'keyboard',
        'Buttons': [
            {
                'ActionBody': 'action body',
                'Columns': 6,
                'Rows': 1,
                'ActionType': 'reply',
                'Text': 'text',
            }
        ],
        'BgColor': '#000000',
        'DefaultHeight': False,
        'CustomDefaultHeight': 70,
        'HeightScale': 100,
        'ButtonsGroupColumns': 6,
        'ButtonsGroupRows': 2,
        'InputFieldState': 'regular'
    }

    obj = Keyboard(**expected)
    assert type(obj.buttons[0]) == Button
    assert obj.serialize() == expected
