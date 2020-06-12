from cliglue import CliBuilder, argument, parameter, subcommand
from cliglue.types.filesystem import existing_file

from trimmer.upgrade import upgrade
from .trim_mp3 import trim_mp3
from .trim_url import trim_url
from .version import __version__


def main():
    CliBuilder('trimmer', version=__version__, help='Automatic song processing tool').has(
        subcommand('url', help='download & trim one song', run=trim_url).has(
            argument('url', help='song youtube url', type=str),
            parameter('artist', help='song artist', type=str),
            parameter('title', help='song title', type=str),
        ),
        subcommand('mp3', help='trim already downloaded song', run=trim_mp3).has(
            argument('file', help='MP3 filename', type=existing_file),
            parameter('artist', help='song artist', type=str),
            parameter('title', help='song title', type=str),
            parameter('trim-start', help='trim seconds at the beginning', type=float),
            parameter('trim-end', help='trim seconds at the end', type=float),
        ),
        subcommand('upgrade', help='upgrade dependencies', run=upgrade),
    ).run()
