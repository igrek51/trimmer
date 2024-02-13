import os
import shutil

import eyed3
from pydub import AudioSegment

from trimmer.trim_source import trim_from_source


def test_trim_from_file():
    shutil.copyfile('./tests/tubular_showcase_bad.mp3', './tests/result_tubular_showcase_bad.mp3')
    source = './tests/result_tubular_showcase_bad.mp3'
    assert os.path.isfile(source), 'source file should exist'

    trim_from_source(source, artist='result_Mike', title=None,
                     no_trim=False, no_fade=False, no_normalize=False, no_rename=False,
                     trim_start=None, trim_end=None, gain=None, output=None)

    assert not os.path.isfile(source), 'source file should not exist any longer'
    output = './tests/result_Mike - Tubular Bells Part I (2003).mp3'
    assert os.path.isfile(output), 'output file should exist'

    song = AudioSegment.from_mp3(output)
    assert -0.6 < song.max_dBFS < 0.6, 'volume should be normalized'
    assert 75 < len(song) / 1000 < 76, 'silence should be trimmed'

    audiofile = eyed3.load(output)
    assert audiofile.tag.artist == 'result_Mike'
    assert audiofile.tag.title == 'Tubular Bells Part I (2003)'
