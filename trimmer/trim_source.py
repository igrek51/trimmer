import os
import re
from typing import Optional

from trimmer.downloader import download_from_youtube, extract_youtube_artist_title
from trimmer.normalizer import normalize_song
from trimmer.renamer import rename_song
from trimmer.sublog.sublog import info, log_error, wrap_context
from trimmer.tagger import read_mp3_tags
from trimmer.tagger import tag_mp3


def trim_from_source(source: str, artist: Optional[str], title: Optional[str],
                     no_trim: bool, no_fade: bool, no_normalize: bool,
                     trim_start: Optional[float], trim_end: Optional[float]):
    with log_error():
        if source_is_url(source):
            info('source recognized as url', source=source)
            trim_url(source, artist, title, no_trim, no_fade, no_normalize, trim_start, trim_end)
        elif source_is_mp3(source):
            info('source recognized as mp3 file', source=source)
            trim_mp3(source, artist, title, no_trim, no_fade, no_normalize, trim_start, trim_end)
        else:
            raise RuntimeError(f'unrecognized source: {source}')


def trim_url(url: str, artist: Optional[str], title: Optional[str],
             no_trim: bool, no_fade: bool, no_normalize: bool,
             trim_start: Optional[float] = None, trim_end: Optional[float] = None):
    with wrap_context('url song'):
        yt_artist, yt_title = extract_youtube_artist_title(url)
        artist = artist or enter_or_default('Artist', default=yt_artist)
        title = title or enter_or_default('Title', default=yt_title)

        mp3_file = download_from_youtube(url)
        mp3_file = rename_song(mp3_file, artist, title)
        normalize_song(mp3_file, no_trim, no_fade, no_normalize, trim_start, trim_end)
        tag_mp3(mp3_file, artist, title)

        info('song saved', mp3_file=mp3_file)


def trim_mp3(file: str, artist: Optional[str], title: Optional[str],
             no_trim: bool, no_fade: bool, no_normalize: bool,
             trim_start: Optional[float] = None, trim_end: Optional[float] = None):
    with wrap_context('mp3 song'):
        assert os.path.isfile(file), 'input file should exist'

        tag_artist, tag_title = read_mp3_tags(file)
        artist = artist or tag_artist or input('Artist: ')
        title = title or tag_title or input('Title: ')

        mp3_file = rename_song(file, artist, title)
        normalize_song(mp3_file, no_trim, no_fade, no_normalize, trim_start, trim_end)
        tag_mp3(mp3_file, artist, title)

        info('song saved', mp3_file=mp3_file)


def source_is_url(source: str) -> bool:
    regex = re.compile(r'^(?:http|ftp)s?://')
    return re.match(regex, source) is not None


def source_is_mp3(source: str) -> bool:
    return source.lower().endswith('.mp3')


def enter_or_default(prompt_name: str, default: str = None) -> str:
    prompt = f'Enter {prompt_name} ("{default}" by default): ' if default else f'Enter {prompt_name}: '
    value = input(prompt)
    if not value:
        return default
    return value
