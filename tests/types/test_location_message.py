from viber_botapi.types import LocationMessage, Location


def test_location_message():
    expected = {
        'type': 'location',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'location': {
            'lat': '37.7898',
            'lon': '-122.3942'
        }
    }

    obj = LocationMessage(**expected)

    assert type(obj.location) == Location
    assert obj.serialize(add_min_api_ver=True) == expected
