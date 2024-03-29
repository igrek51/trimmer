from trimmer.metadata import extract_artist_title, trim_parentheses


def test_trimming_dots_spaces():
    artist, title = extract_artist_title('   Rick Astley -    Never Gonna Give You Up....')
    assert artist == 'Rick Astley'
    assert title == 'Never Gonna Give You Up'


def test_removing_brackets():
    artist, title = extract_artist_title('Pink Floyd - Welcome To The Machine (Live, Delicate Sound Of Thunder) [2019 Remix]')
    assert artist == 'Pink Floyd'
    assert title == 'Welcome To The Machine'


def test_trim_parentheses():
    assert trim_parentheses('Welcome To The Machine (Live at Pompeii)') == 'Welcome To The Machine'
