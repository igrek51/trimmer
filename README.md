# Trimmer
MP3 song normalizer

[![GitHub version](https://badge.fury.io/gh/igrek51%2Ftrimmer.svg)](https://github.com/igrek51/trimmer)
[![PyPI version](https://badge.fury.io/py/trimmer.svg)](https://pypi.org/project/trimmer)
[![Github Pages](https://img.shields.io/badge/docs-github.io-blue)](https://igrek51.github.io/trimmer)
[![Build Status](https://travis-ci.org/igrek51/trimmer.svg?branch=master)](https://travis-ci.org/igrek51/trimmer)
[![codecov](https://codecov.io/gh/igrek51/trimmer/branch/master/graph/badge.svg)](https://codecov.io/gh/igrek51/trimmer)


Are you tired of quiet songs on Youtube with long silence before or after song? 

Trimmer does the following things:

1. Downloads songs from given Youtube URL (thanks to [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [yt-dlp](https://github.com/yt-dlp/yt-dlp))
2. Trims down silence at the beginning & at the end of song (thanks to [pydub](https://github.com/jiaaro/pydub))
3. Normalizes volume level (detecting clipping), applies fade-in & fade-out (thanks to [pydub](https://github.com/jiaaro/pydub))
4. Adds MP3 ID3 tags - both ID3v1 & ID3v2 (thanks to [eyed3](https://github.com/nicfit/eyeD3))
5. Creates mp3 file named: `Artist - Title.mp3`

## Downloading MP3
Create trimmed, normalized & tagged mp3 from Youtube URL:
```shell
trimmer https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
![Usage example](https://github.com/igrek51/trimmer/blob/master/docs/img/screenshot-1.png?raw=true)

## Editing MP3
```shell
trimmer "unknown001.mp3"
```

From this:  
**unknown001.mp3**  
![Usage example](https://github.com/igrek51/trimmer/blob/master/docs/img/song_amp_bad.png?raw=true)  
trimmer does that:  
**Mike Oldfield - Tubular Bells Part I.mp3**  
![Usage example](https://github.com/igrek51/trimmer/blob/master/docs/img/song_amp_good.png?raw=true)

You can also trim song manually using `--trim-start` and `--trim-end` (e.g. for cutting long applause at the end of song).

## Installation
```shell
pip3 install trimmer
```

It requires Python 3.6 (or newer) with pip.

For Linux make sure that required libs are installed: `apt install ffmpeg libavcodec-extra`

For Windows you might need to put [ffmpeg binaries](https://ffmpeg.zeranoe.com/builds/) to `PATH`.

## Upgrading
Keep up-to-date frequently changing dependencies (due to Youtube API changes):
```shell
pip3 install --upgrade --upgrade-strategy eager trimmer
```

## Help
```shell
$ trimmer --help
trimmer v1.0.0 (nuclear v1.3.4) - MP3 song normalizer

Usage:
trimmer [OPTIONS] SOURCE

Arguments:
   SOURCE - song source (youtube URL or MP3 file)

Options:
  --version                   - Print version information and exit
  -h, --help [SUBCOMMANDS...] - Display this help and exit
  --artist ARTIST             - song artist
  --title TITLE               - song title
  --trim-start TRIM_START     - trim given seconds at the beginning
  --trim-end TRIM_END         - trim given seconds at the end
  --gain GAIN                 - increase volume by given dB
  --output OUTPUT             - output MP3 file (Artist - Title.mp3 by default)
  --no-normalize              - skip normalizing volume level
  --no-trim                   - skip trimming silence at the edges of song
  --no-fade                   - skip applying fade-in & fade-out
  --no-rename                 - skip renaming song to normalized filename (Artist - Title.mp3)
```

## Install locally in develop mode
```shell
make setup
. venv/bin/activate
```
