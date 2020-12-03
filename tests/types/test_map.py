from viber_botapi.types import Map


def test_map():
    expected = {
        'Latitude': '37.7898',
        'Longitude': '-122.3942',
        'min_api_version': 6
    }

    data1 = {
        'Latitude': '37.7898',
        'Longitude': '-122.3942',
    }

    obj = Map(**data1)
    assert obj.serialize(add_min_api_ver=True) == expected

    data2 = {
        'latitude': '37.7898',
        'longitude': '-122.3942',
    }

    obj = Map(**data2)
    assert obj.serialize(add_min_api_ver=True) == expected
