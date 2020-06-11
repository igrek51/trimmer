from typing import Optional

from trimmer.normalizer import normalize_song
from trimmer.renamer import rename_song
from trimmer.sublog import info, log_error, wrap_context
from trimmer.tagger import tag_mp3
from trimmer.yt_downloader import download_from_youtube


def trim_url(url: str, artist: Optional[str], title: Optional[str]):
    with log_error():
        with wrap_context('url song'):
            artist = artist or input('Artist: ')
            title = title or input('Title: ')

            mp3_file = download_from_youtube(url)
            mp3_file = rename_song(mp3_file, artist, title)
            normalize_song(mp3_file)
            tag_mp3(mp3_file, artist, title)

            info('song saved', mp3_file=mp3_file)
