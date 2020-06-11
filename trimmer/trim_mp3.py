import os
from typing import Optional

from trimmer.normalizer import normalize_song
from trimmer.renamer import rename_song
from trimmer.sublog import info, log_error, wrap_context
from trimmer.tagger import tag_mp3, read_mp3_tags


def trim_mp3(file: str, artist: Optional[str], title: Optional[str],
             trim_start: Optional[float], trim_end: Optional[float]):
    with log_error():
        with wrap_context('url song'):
            assert os.path.isfile(file), 'file should exist'

            tag_artist, tag_title = read_mp3_tags(file)

            artist = artist or tag_artist or input('Artist: ')
            title = title or tag_title or input('Title: ')

            mp3_file = rename_song(file, artist, title)
            normalize_song(mp3_file, trim_start=trim_start, trim_end=trim_end)
            tag_mp3(mp3_file, artist, title)

            info('song saved', mp3_file=mp3_file)
