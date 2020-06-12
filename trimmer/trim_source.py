import os
import re
from typing import Optional

from trimmer.normalizer import normalize_song
from trimmer.renamer import rename_song
from trimmer.sublog import info, log_error, wrap_context
from trimmer.tagger import read_mp3_tags
from trimmer.tagger import tag_mp3
from trimmer.yt_downloader import download_from_youtube


def trim_from_source(source: str, artist: Optional[str], title: Optional[str],
                     trim_start: Optional[float], trim_end: Optional[float]):
    with log_error():
        if source_is_url(source):
            trim_url(source, artist, title, trim_start, trim_end)
        elif source_is_mp3(source):
            trim_mp3(source, artist, title, trim_start, trim_end)
        else:
            raise RuntimeError(f'unrecognized source: {source}')


def trim_url(url: str, artist: Optional[str], title: Optional[str],
             trim_start: Optional[float] = None, trim_end: Optional[float] = None):
    with wrap_context('url song'):
        artist = artist or input('Artist: ')
        title = title or input('Title: ')

        mp3_file = download_from_youtube(url)
        mp3_file = rename_song(mp3_file, artist, title)
        normalize_song(mp3_file, trim_start=trim_start, trim_end=trim_end)
        tag_mp3(mp3_file, artist, title)

        info('song saved', mp3_file=mp3_file)


def trim_mp3(file: str, artist: Optional[str], title: Optional[str],
             trim_start: Optional[float] = None, trim_end: Optional[float] = None):
    with wrap_context('url song'):
        assert os.path.isfile(file), 'input file should exist'

        tag_artist, tag_title = read_mp3_tags(file)

        artist = artist or tag_artist or input('Artist: ')
        title = title or tag_title or input('Title: ')

        mp3_file = rename_song(file, artist, title)
        normalize_song(mp3_file, trim_start=trim_start, trim_end=trim_end)
        tag_mp3(mp3_file, artist, title)

        info('song saved', mp3_file=mp3_file)


def source_is_url(source: str) -> bool:
    regex = re.compile(r'^(?:http|ftp)s?://')
    return re.match(regex, source) is not None


def source_is_mp3(source: str) -> bool:
    return source.lower().endswith('.mp3')
