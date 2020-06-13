# Trimmer
[![GitHub version](https://badge.fury.io/gh/igrek51%2Ftrimmer.svg)](https://github.com/igrek51/trimmer)
[![PyPI version](https://badge.fury.io/py/trimmer.svg)](https://pypi.org/project/trimmer)
[![Documentation Status](https://readthedocs.org/projects/trimmer-py/badge/?version=latest)](https://trimmer-py.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/igrek51/trimmer.svg?branch=master)](https://travis-ci.org/igrek51/trimmer)
[![Coverage Status](https://coveralls.io/repos/github/igrek51/trimmer/badge.svg?branch=master)](https://coveralls.io/github/igrek51/trimmer?branch=master)

MP3 song normalizer

trimmer does the following things:
1. Downloads songs from given youtube URL (thanks to [youtube-dl](https://github.com/ytdl-org/youtube-dl))
2. Trims down silence at the beginning & at the end of song (thanks to [pydub](https://github.com/jiaaro/pydub))
3. Normalizes volume level, applies fade-in & fade-out (thanks to [pydub](https://github.com/jiaaro/pydub))
4. Adds MP3 ID3v2 tags (thanks to [eyed3](https://github.com/nicfit/eyeD3))
5. Creates mp3 file named: `Artist - Title.mp3`

# Usage
## Downloading MP3 from YouTube URL
Create trimmed, normalized, tagged mp3:
```shell
trimmer https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
![Usage example](https://github.com/igrek51/trimmer/blob/master/docs/img/screenshot-1.png)

## Editing MP3
Trim down manually (e.g. long applause at the end of song)
```shell
trimmer "Rick Astley - Never Gonna Give You Up.mp3" --trim-end 30
```

## Help
```shell
$ trimmer --help
trimmer v0.1.3 (cliglue v1.0.8) - Automatic song processing tool

Usage:
/mnt/data/Igrek/python/trimmer/venv/bin/trimmer [OPTIONS] SOURCE

Arguments:
   SOURCE - song source (youtube URL or MP3 file)

Options:
  --version                   - Print version information and exit
  -h, --help [SUBCOMMANDS...] - Display this help and exit
  --artist ARTIST             - song artist
  --title TITLE               - song title
  --trim-start TRIM_START     - trim given seconds at the beginning
  --trim-end TRIM_END         - trim given seconds at the end
  --upgrade                   - upgrade dependencies & exit
```

# Installation
```shell
pip3 install trimmer
```

Requirements:
* Python 3.6 (or newer) with pip

## Upgrading
```
pip3 install --upgrade trimmer
```

## Install locally in develop mode
```shell
./setup_venv.sh
. venv/bin/activate
python setup.py develop
```

# TODO
- idempotent trimming (not trimming fade-outs again)
