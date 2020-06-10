from typing import Optional

from trimmer.mp3_normalizer import Mp3Normalizer
from trimmer.mp3_renamer import Mp3Renamer
from trimmer.mp3_tagger import Mp3Tagger
from trimmer.sublog import info, log_error, wrap_context
from trimmer.yt_downloader import YoutubeDownloader


def trim_url(url: str, artist: Optional[str], title: Optional[str]):
    with log_error():
        if not artist:
            artist = input('Artist: ')
        if not title:
            artist = input('Title: ')

        with wrap_context('downloading from youtube', url=url):
            info('downloading from youtube...', url=url)
            mp3_file = YoutubeDownloader().download(url)

        with wrap_context('renaming mp3', artist=artist, title=title, mp3_file=mp3_file):
            info('renaming mp3...', artist=artist, title=title, mp3_file=mp3_file)
            mp3_file = Mp3Renamer().rename(mp3_file, artist, title)

        with wrap_context('normalizing mp3', mp3_file=mp3_file):
            info('normalizing mp3...', mp3_file=mp3_file)
            Mp3Normalizer().normalize(mp3_file)

        with wrap_context('tagging mp3', artist=artist, title=title, mp3_file=mp3_file):
            info('tagging mp3...', artist=artist, title=title, mp3_file=mp3_file)
            Mp3Tagger().tag(mp3_file, artist, title)

        info('success')
