from viber_botapi.types import RichMedia, Button, FavoritesMetadata


def test_rich_media_serialize():
    expected = {
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
        'FavoritesMetadata': {
            'type': 'link',
            'url': 'https://en.wikipedia.org/wiki/Viber',
            'title': 'Interesting article about Viber',
            'thumbnail': 'https://www.viber.com/app/uploads/icon-purple.png',
            'domain': 'www.wikipedia.org',
            'width': 480,
            'height': 320,
            'alternativeUrl': 'https://www.viber.com/about/',
            'alternativeText': 'About Viber'
        }
    }

    obj = RichMedia(**expected)
    assert type(obj.buttons[0]) == Button
    assert type(obj.favorites_metadata) == FavoritesMetadata
    assert obj.serialize() == expected
