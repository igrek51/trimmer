from trimmer.metadata import extract_artist_title


def test_trimming_dots_spaces():
    artist, title = extract_artist_title('   Rick Astley -    Never Gonna Give You Up....')
    assert artist == 'Rick Astley'
    assert title == 'Never Gonna Give You Up'


def test_removing_brackets():
    artist, title = extract_artist_title('Pink Floyd - Welcome To The Machine (Live, Delicate Sound Of Thunder) [2019 Remix]')
    assert artist == 'Pink Floyd'
    assert title == 'Welcome To The Machine'
