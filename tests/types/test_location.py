from viber_botapi.types import Location


def test_to_dict():
    expected = {
        'lat': '37.7898',
        'lon': '-122.3942'
    }
    obj = Location(**expected)
    assert obj.serialize() == expected
