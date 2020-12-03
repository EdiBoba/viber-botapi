import pytest

from viber_botapi.types import Frame


def test_frame():
    data = {
        'BorderWidth': 1,
        'BorderColor': '#000000',
        'CornerRadius': 0,
    }

    obj = Frame(**data)

    with pytest.raises(TypeError):
        obj.border_width = 'not int'

    with pytest.raises(TypeError):
        obj.border_color = 123

    with pytest.raises(TypeError):
        obj.corner_radius = 'not int'

    expected = {
        'BorderWidth': 1,
        'BorderColor': '#000000',
        'CornerRadius': 0,
        'min_api_version': 6
    }

    assert obj.serialize(add_min_api_ver=True) == expected
