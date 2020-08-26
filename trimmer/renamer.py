import os
from pathlib import Path

from nuclear.sublog import wrap_context, log


def rename_song(mp3_file: str, artist: str, title: str) -> str:
    with wrap_context('renaming song', artist=artist, title=title, mp3_file=mp3_file):
        dirname, filename = os.path.split(mp3_file)
        if artist.strip():
            new_filename = f'{artist.strip()} - {title.strip()}.mp3'
        else:
            new_filename = f'{title.strip()}.mp3'
        new_path = Path(dirname) / new_filename
        os.rename(mp3_file, new_path)
        log.info('song renamed', new_name=new_path)
        return new_path


def rename_output_song(mp3_file: str, output: str) -> str:
    with wrap_context('renaming song', mp3_file=mp3_file, output=output):
        os.rename(mp3_file, output)
        log.info('song renamed', new_name=output)
        return output
