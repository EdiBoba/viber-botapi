import pytest

from viber_botapi.types import FileMessage


def test_file_message():
    data = {
        'tracking_data': 'tracking data',
        'media': 'http://www.images.com/file.doc',
        'size': 10000,
        'file_name': 'name_of_file.doc'
    }
    obj = FileMessage(**data)

    with pytest.raises(TypeError):
        obj.media = 123

    with pytest.raises(TypeError):
        obj.size = 'not int'

    with pytest.raises(TypeError):
        obj.file_name = 123

    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'file',
        'media': 'http://www.images.com/file.doc',
        'size': 10000,
        'file_name': 'name_of_file.doc'
    }
    assert obj.serialize(add_min_api_ver=True) == expected
