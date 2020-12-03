from viber_botapi.types import Contact, ContactMessage


def test_contact_message_serialize():
    contact = Contact(name='Itamar', phone_number='+972511123123')
    obj = ContactMessage(contact=contact, tracking_data='tracking data')
    expected = {
        'type': 'contact',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'contact': {
            'name': 'Itamar',
            'phone_number': '+972511123123'
        }
    }
    assert obj.serialize(add_min_api_ver=True) == expected

    obj = ContactMessage(**expected)

    assert type(obj.contact) == Contact
    assert obj.serialize(add_min_api_ver=True) == expected
