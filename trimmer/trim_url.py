from typing import Optional

from trimmer.mp3_normalizer import Mp3Normalizer
from trimmer.mp3_renamer import Mp3Renamer
from trimmer.mp3_tagger import Mp3Tagger
from trimmer.sublog import info, log_error
from trimmer.yt_downloader import YoutubeDownloader


def trim_url(url: str, artist: Optional[str], title: Optional[str]):
    with log_error():
        if not artist:
            artist = input('Artist: ')
        if not title:
            artist = input('Title: ')

    info('downloading from url', url=url)
    mp3_file = YoutubeDownloader().download(url)
    mp3_file = Mp3Renamer().rename(mp3_file, artist, title)
    Mp3Normalizer().normalize(mp3_file)
    Mp3Tagger().tag(mp3_file, artist, title)
