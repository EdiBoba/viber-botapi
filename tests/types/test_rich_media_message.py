from viber_botapi.types import RichMediaMessage, RichMedia


def test_rich_media_message_serialize():
    expected = {
        'min_api_version': 7,
        'type': 'rich_media',
        'rich_media': {
            'Buttons': [{
                'ActionBody': 'action body',
                'Columns': 6,
                'Rows': 1,
                'ActionType': 'reply',
                'Text': 'text',
            }],
            'ButtonsGroupColumns': 6,
            'ButtonsGroupRows': 7,
            'BgColor': '#000000',
            'Type': 'rich_media',
        },
        'alt_text': 'alt text',
        'tracking_data': 'tracking data'
    }

    obj = RichMediaMessage(**expected)
    assert type(obj.rich_media) == RichMedia
    assert obj.serialize(add_min_api_ver=True) == expected
