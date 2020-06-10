import os

import youtube_dl


def test_youtube_dl():
    url = 'https://www.youtube.com/watch?v=omafc3SazWA'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/tmp/trimmer_dl_1234.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        print(result)

    assert os.path.isfile('/tmp/trimmer_dl_1234.mp3')
    os.remove('/tmp/trimmer_dl_1234.mp3')
