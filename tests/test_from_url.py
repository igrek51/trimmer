import os
import sys

import eyed3
from pydub import AudioSegment

from trimmer.trim_source import trim_url


def test_trim_from_url():
    # workaround for travis + python stdout opened in rb+ mode
    sys.stdout = open(sys.stdout.fileno(), mode='r+', encoding='utf8', buffering=1)

    url = 'https://www.youtube.com/watch?v=omafc3SazWA'
    trim_url(url, artist='Stachu Jones', title='O kurna')

    filename = 'Stachu Jones - O kurna.mp3'
    assert os.path.isfile(filename), 'output file should exist'

    song = AudioSegment.from_mp3(filename)
    assert -0.6 < song.max_dBFS < 0.6, 'volume should be normalized'
    assert 1.2 < len(song) / 1000 < 1.5, 'silence should be trimmed'

    audiofile = eyed3.load(filename)
    assert audiofile.tag.artist == 'Stachu Jones'
    assert audiofile.tag.title == 'O kurna'

    os.remove(filename)
