import os
from pathlib import Path

from trimmer.sublog.sublog import wrap_context, info


def rename_song(mp3_file: str, artist: str, title: str) -> str:
    with wrap_context('renaming song', artist=artist, title=title, mp3_file=mp3_file):
        dirname, filename = os.path.split(mp3_file)
        new_filename = f'{artist.strip()} - {title.strip()}.mp3'
        new_path = Path(dirname) / new_filename
        os.rename(mp3_file, new_path)
        info('song renamed', new_name=new_path)
        return new_path
