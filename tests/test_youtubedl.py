import os
import sys

import youtube_dl


def test_youtube_dl_download():
    # workaround for travis + python stdout opened in rb+ mode
    # sys.stdout = open(sys.stdout.fileno(), mode='r+', encoding='utf8', buffering=1)

    url = 'https://www.youtube.com/watch?v=omafc3SazWA'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/tmp/trimmer_dl_1234.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        print(result)

    assert os.path.isfile('/tmp/trimmer_dl_1234.mp3')
    os.remove('/tmp/trimmer_dl_1234.mp3')


def test_youtube_dl_title():
    # workaround for travis + python stdout opened in rb+ mode
    # sys.stdout = open(sys.stdout.fileno(), mode='r+', encoding='utf8', buffering=1)

    url = 'https://www.youtube.com/watch?v=omafc3SazWA'
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
        print('ydl._screen_file', ydl._screen_file)
        print('ydl._screen_file.mode', ydl._screen_file.mode)
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        title = filename[:-4]
        assert title == 'O KURWA'
