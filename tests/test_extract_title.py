import sys

from trimmer.downloader import extract_youtube_artist_title


def test_extract_title():
    # workaround for travis + python stdout opened in rb+ mode
    # sys.stdout = open(sys.stdout.fileno(), mode='r+', encoding='utf8', buffering=1)

    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    artist, title = extract_youtube_artist_title(url)
    assert artist == 'Rick Astley'
    assert title == 'Never Gonna Give You Up'
