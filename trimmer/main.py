from cliglue import CliBuilder, argument, parameter, flag

from .trim_source import trim_from_source
from .version import __version__


def main():
    CliBuilder('trimmer', version=__version__, help='Automatic song processing tool',
               run=trim_from_source, help_on_empty=True).has(
        argument('source', help='song source (youtube URL or MP3 file)'),
        parameter('artist', help='song artist', type=str),
        parameter('title', help='song title', type=str),
        parameter('trim-start', help='trim given seconds at the beginning', type=float),
        parameter('trim-end', help='trim given seconds at the end', type=float),
        flag('no-normalize', help='skip normalizing volume level'),
        flag('no-trim', help='skip trimming silence at the edges of song'),
        flag('no-fade', help='skip applying fade-in & fade-out'),
    ).run()
