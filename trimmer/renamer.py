import os

from trimmer.sublog import wrap_context, info


def rename_song(mp3_file: str, artist: str, title: str) -> str:
    with wrap_context('renaming song mp3', artist=artist, title=title, mp3_file=mp3_file):
        new_filename = f'{artist.strip()} - {title.strip()}.mp3'
        os.rename(mp3_file, new_filename)
        info('song renamed', filename=new_filename)

        return new_filename
