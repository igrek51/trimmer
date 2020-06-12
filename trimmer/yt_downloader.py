import os
import uuid
from typing import Tuple

import youtube_dl

from trimmer.sublog import wrap_context, info


def download_from_youtube(url: str) -> str:
    with wrap_context('downloading from youtube', url=url):
        info('downloading from youtube...', url=url)

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
        info('song downloaded', tmpfile=full_filename)

        return full_filename


def fetch_youtube_title(url: str) -> str:
    with wrap_context('fetching title from youtube', url=url):
        info('fetching title from youtube...', url=url)

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
            filename = ydl.prepare_filename(einfo)
            title = filename[:-4]
            info('youtube title fetched', yt_title=title)
            return title


def extract_youtube_artist_title(url: str) -> Tuple[str, str]:
    yt_title = fetch_youtube_title(url)

    if '-' not in yt_title:
        return '', yt_title.strip()
    dash_index = yt_title.find('-')
    artist = yt_title[:dash_index].strip()
    title = yt_title[dash_index + 1:].strip()
    info('artist & title extracted from youtube page', artist=artist, title=title)
    return artist, title
