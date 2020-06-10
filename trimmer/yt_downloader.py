import os
import uuid

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
        info('song downloaded', filename=full_filename)

        return full_filename
