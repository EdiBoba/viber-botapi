from botapi import Field

from viber_botapi.types import ViberModel


def test_update_data():
    class TestModel(ViberModel):
        field = Field(default='field')

    expected = {
        'field': 'field',
        'updated_field': 'new_field'
    }

    obj = TestModel()
    assert obj.serialize(data_to_update={'updated_field': 'new_field'}) == expected
