import os
from typing import Tuple

import eyed3
from eyed3.id3 import ID3_V2_4, ID3_V1_1

from trimmer.metadata import extract_artist_title
from trimmer.sublog.sublog import wrap_context, info, warn


def tag_mp3(mp3_file: str, artist: str, title: str):
    with wrap_context('tagging mp3', artist=artist, title=title, mp3_file=mp3_file):
        info('tagging mp3...', artist=artist, title=title)

        audiofile = eyed3.load(mp3_file)
        audiofile.tag.artist = artist
        audiofile.tag.title = title

        audiofile.tag.save(version=ID3_V1_1)
        audiofile.tag.save(version=ID3_V2_4)


def read_mp3_artist_title(mp3_file: str) -> Tuple[str, str]:
    with wrap_context('extracting mp3 metadata', mp3_file=mp3_file):
        tag_artist, tag_title = read_mp3_tags(mp3_file)
        file_artist, file_title = extract_filename_artist_title(mp3_file)
        artist = tag_artist or file_artist
        title = tag_title or file_title
        info('metadata inferred', artist=artist, title=title)
        return artist, title


def read_mp3_tags(mp3_file: str) -> Tuple[str, str]:
    with wrap_context('reading mp3 tags'):

        audiofile = eyed3.load(mp3_file)
        if audiofile is None or audiofile.tag is None:
            warn('no IDv3 tags read', mp3_file=mp3_file)
            return '', ''

        artist = audiofile.tag.artist.strip()
        title = audiofile.tag.title.strip()
        info('IDv3 tags read', mp3_file=mp3_file, artist=artist, title=title)
        return artist, title


def extract_filename_artist_title(mp3_file: str) -> Tuple[str, str]:
    with wrap_context('extracting metadata from filename'):
        _, filename = os.path.split(mp3_file)
        if filename.lower().endswith('.mp3'):
            filename = mp3_file[:-4]
        return extract_artist_title(filename)
