import os
import uuid
from typing import Tuple

import youtube_dl
import yt_dlp
from nuclear.sublog import wrap_context, log

from trimmer.metadata import extract_artist_title, trim_parentheses


def download_from_youtube(url: str) -> str:
    with wrap_context('downloading from youtube', url=url):
        log.info('downloading from youtube...', url=url)

        uid = str(uuid.uuid4())
        filename = f'trimmer_dl_{uid}'

        _download_url(url, filename)

        full_filename = f'{filename}.mp3'
        assert os.path.isfile(full_filename), "target file doesn't exist"
        log.info('song downloaded', tmpfile=full_filename)

        return full_filename


def extract_youtube_artist_title(url: str) -> Tuple[str, str]:
    artist, track, full_title = _fetch_youtube_metadata(url)
    if artist and track:
        return artist, trim_parentheses(track)

    return extract_artist_title(full_title)


def _fetch_youtube_metadata(url: str) -> Tuple[str, str, str]:
    with wrap_context('fetching metadata from youtube', url=url):
        log.info('fetching metadata from youtube page...', url=url)
        artist, track, full_title = _extract_url_info(url)
        log.info('youtube page metadata fetched', yt_title=full_title, artist=artist, track=track)
        return artist, track, full_title


def _download_url(url: str, out_filename: str):
    try:
        _download_url_yt_dlp(url, out_filename)
    except Exception as e:
        log.warn('yt_dlp lib failed, trying again with youtube_dl', error=str(e))
        _download_url_youtube_dl(url, out_filename)


def _download_url_youtube_dl(url: str, out_filename: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{out_filename}.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        retcode = ydl.download([url])
        assert retcode == 0, 'youtube_dl exited with error'


def _download_url_yt_dlp(url: str, out_filename: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{out_filename}.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        retcode = ydl.download([url])
        assert retcode == 0, 'yt_dlp exited with error'


def _extract_url_info(url: str) -> Tuple[str, str, str]:
    try:
        return _extract_url_info_yt_dlp(url)
    except Exception as e:
        log.warn('yt_dlp lib failed, trying again with youtube_dl', error=str(e))
        return _extract_url_info_youtube_dl(url)


def _extract_url_info_youtube_dl(url: str) -> Tuple[str, str, str]:
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
        return artist, track, full_title


def _extract_url_info_yt_dlp(url: str) -> Tuple[str, str, str]:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        einfo = ydl.extract_info(url, download=False)
        track = einfo.get('track')
        artist = einfo.get('artist') or einfo.get('creator')
        full_title = einfo.get('title') or einfo.get('alt_title')
        return artist, track, full_title