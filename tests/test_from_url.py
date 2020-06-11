import os

from trimmer.trim_url import trim_url


def test_trim_from_url():
    url = 'https://www.youtube.com/watch?v=omafc3SazWA'
    trim_url(url, artist='Stachu Jones', title='O kurna')

    assert os.path.isfile('Stachu Jones - O kurna.mp3')
