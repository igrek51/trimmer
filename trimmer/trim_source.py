import os
import re
import shutil
from typing import Optional

from nuclear.sublog import log, log_error, wrap_context

from trimmer.downloader import download_from_youtube, extract_youtube_artist_title
from trimmer.normalizer import normalize_song
from trimmer.renamer import rename_song, rename_output_song
from trimmer.tagger import read_mp3_artist_title
from trimmer.tagger import tag_mp3


def trim_from_source(source: str, artist: Optional[str], title: Optional[str],
                     no_trim: bool, no_fade: bool, no_normalize: bool, no_rename: bool,
                     trim_start: Optional[float], trim_end: Optional[float], gain: Optional[float],
                     output: Optional[str]):
    with log_error():
        if source_is_url(source):
            log.info('source recognized as url', source=source)
            trim_url(source, artist, title, no_trim, no_fade, no_normalize,
                     trim_start, trim_end, gain, output)
        elif source_is_mp3(source):
            log.info('source recognized as mp3 file', source=source)
            trim_mp3(source, artist, title, no_trim, no_fade, no_normalize, no_rename,
                     trim_start, trim_end, gain, output)
        else:
            raise RuntimeError(f'unrecognized source: {source}')


def trim_url(url: str, user_artist: Optional[str], user_title: Optional[str],
             no_trim: bool, no_fade: bool, no_normalize: bool,
             trim_start: Optional[float], trim_end: Optional[float], gain: Optional[float], output: Optional[str]):
    with wrap_context('url song'):
        yt_artist, yt_title = extract_youtube_artist_title(url)
        log.info('artist & title extracted from youtube page', artist=yt_artist, title=yt_title)
        artist = user_artist or enter_or_default('Artist', default=yt_artist)
        title = user_title or enter_or_default('Title', default=yt_title)

        mp3_file = download_from_youtube(url)
        if output:
            mp3_file = rename_output_song(mp3_file, output)
        else:
            mp3_file = rename_song(mp3_file, artist, title)
        normalize_song(mp3_file, no_trim, no_fade, no_normalize, trim_start, trim_end, gain)
        tag_mp3(mp3_file, artist, title)

        log.info('song saved', mp3_file=mp3_file)


def trim_mp3(mp3_file: str, user_artist: Optional[str], user_title: Optional[str],
             no_trim: bool, no_fade: bool, no_normalize: bool, no_rename: bool,
             trim_start: Optional[float], trim_end: Optional[float], gain: Optional[float], output: Optional[str]):
    with wrap_context('mp3 song'):
        assert os.path.isfile(mp3_file), 'input file should exist'

        if output:
            shutil.copyfile(mp3_file, output)
            mp3_file = output

        tag_artist, tag_title = read_mp3_artist_title(mp3_file)
        artist = user_artist or tag_artist or enter_or_default('Artist', default='')
        title = user_title or tag_title or enter_or_default('Title', default='')

        if not output and not no_rename:
            mp3_file = rename_song(mp3_file, artist, title)
        normalize_song(mp3_file, no_trim, no_fade, no_normalize, trim_start, trim_end, gain)
        tag_mp3(mp3_file, artist, title)

        log.info('song saved', mp3_file=mp3_file)


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
