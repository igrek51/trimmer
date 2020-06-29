import os
import uuid
from typing import Tuple

import youtube_dl
from nuclear.sublog import wrap_context, log

from trimmer.metadata import extract_artist_title


def download_from_youtube(url: str) -> str:
    with wrap_context('downloading from youtube', url=url):
        log.info('downloading from youtube...', url=url)

        uid = str(uuid.uuid4())
        filename = f'trimmer_dl_{uid}'

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{filename}.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            retcode = ydl.download([url])
            assert retcode == 0

        full_filename = f'{filename}.mp3'
        assert os.path.isfile(full_filename)
        log.info('song downloaded', tmpfile=full_filename)

        return full_filename


def fetch_youtube_metadata(url: str) -> Tuple[str, str, str]:
    with wrap_context('fetching title from youtube', url=url):
        log.info('fetching metadata from youtube page...', url=url)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            einfo = ydl.extract_info(url, download=False)

            track = einfo.get('track')
            artist = einfo.get('artist') or einfo.get('creator')
            full_title = einfo.get('title') or einfo.get('alt_title')

            log.info('youtube page metadata fetched', yt_title=full_title, artist=artist, track=track)
            return artist, track, full_title


def extract_youtube_artist_title(url: str) -> Tuple[str, str]:
    artist, track, full_title = fetch_youtube_metadata(url)
    if artist and track:
        return artist, track

    return extract_artist_title(full_title)
