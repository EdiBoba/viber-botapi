from viber_botapi.types import FavoritesMetadata


def test_fav_metadata():
    expected = {
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

    obj = FavoritesMetadata(**expected)
    assert obj.serialize() == expected
