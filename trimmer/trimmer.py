#!/usr/bin/env python3

from cliglue import CliBuilder, argument, parameter, subcommand
from cliglue.types.filesystem import existing_file
from cliglue.utils.shell import shell

from trimmer.trim_mp3 import trim_mp3
from trimmer.trim_url import trim_url
from trimmer.version import __version__


def main():
    CliBuilder('trimmer', version=__version__, help='Automatic song processing tool').has(
        subcommand('url', help='download & trim one song', run=trim_url).has(
            argument('url', help='song youtube url', type=str),
            parameter('artist', help='song artist', type=str),
            parameter('title', help='song title', type=str),
        ),
        subcommand('trim', help='trim already downloaded song', run=trim_mp3).has(
            argument('file', help='MP3 filename', type=existing_file),
        ),
        subcommand('upgrade', help='upgrade dependencies', run=upgrade),
    ).run()


def upgrade():
    shell('pip3 install --upgrade youtube-dl')


if __name__ == '__main__':
    main()
