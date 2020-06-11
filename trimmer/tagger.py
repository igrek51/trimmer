from typing import Tuple

import eyed3
from eyed3.id3 import ID3_V2_4, ID3_V1_1

from trimmer.sublog import wrap_context, info, warn


def tag_mp3(mp3_file: str, artist: str, title: str):
    with wrap_context('tagging mp3', artist=artist, title=title, mp3_file=mp3_file):
        info('tagging mp3...', artist=artist, title=title, mp3_file=mp3_file)

        audiofile = eyed3.load(mp3_file)
        audiofile.tag.artist = artist
        audiofile.tag.title = title

        audiofile.tag.save(version=ID3_V1_1)
        audiofile.tag.save(version=ID3_V2_4)


def read_mp3_tags(mp3_file: str) -> Tuple[str, str]:
    with wrap_context('reading mp3 tags', mp3_file=mp3_file):

        audiofile = eyed3.load(mp3_file)
        if audiofile is None:
            warn('no IDv3 tags read', mp3_file=mp3_file)
            return '', ''

        artist = audiofile.tag.artist.strip()
        title = audiofile.tag.title.strip()
        info('IDv3 tags read', mp3_file=mp3_file, artist=artist, title=title)

        return artist, title
