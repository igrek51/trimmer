from trimmer.metadata import extract_artist_title


def test_trimming_dots_spaces():
    artist, title = extract_artist_title('   Rick Astley -    Never Gonna Give You Up....')
    assert artist == 'Rick Astley'
    assert title == 'Never Gonna Give You Up'
