import re
from typing import Tuple

from trimmer.sublog.sublog import info


def extract_artist_title(name: str) -> Tuple[str, str]:
    if '-' not in name:
        return '', name.strip()
    dash_index = name.find('-')

    artist = name[:dash_index].strip()

    title = name[dash_index + 1:].strip()
    title = re.sub(r"\(.+?\)", "", title)
    title = re.sub(r"[. ]+$", "", title)

    info('artist & title extracted from youtube page', artist=artist, title=title)
    return artist, title
