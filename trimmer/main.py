from nuclear import CliBuilder, argument, parameter, flag
from nuclear.completers import file_completer

from .trim_source import trim_from_source
from .version import __version__


def main():
    CliBuilder('trimmer', version=__version__, help='MP3 song normalizer',
               run=trim_from_source, help_on_empty=True).has(
        argument('source', help='song source (youtube URL or MP3 file)', choices=file_completer),
        parameter('artist', help='song artist', type=str),
        parameter('title', help='song title', type=str),
        parameter('trim-start', help='trim given seconds at the beginning', type=float),
        parameter('trim-end', help='trim given seconds at the end', type=float),
        parameter('gain', help='increase volume by given dB', type=float),
        parameter('output', help='output MP3 file (Artist - Title.mp3 by default)'),
        flag('no-normalize', help='skip normalizing volume level'),
        flag('no-trim', help='skip trimming silence at the edges of song'),
        flag('no-fade', help='skip applying fade-in & fade-out'),
        flag('no-rename', help='skip renaming song to normalized filename (Artist - Title.mp3)'),
    ).run()
