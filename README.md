# Trimmer
Songs downloader & normalizer for automatic MP3 processing, which:

1. Downloads mp3 from given youtube URL (thanks to [youtube-dl](https://github.com/ytdl-org/youtube-dl))
2. Trims down silence at the beginning & at the end of song (thanks to [pydub](https://github.com/jiaaro/pydub))
3. Normalizes volume level, applies fade-in & fade-out (thanks to [pydub](https://github.com/jiaaro/pydub))
4. Adds MP3 ID3v2 tags (thanks to [eyed3](https://github.com/nicfit/eyeD3))
5. Creates mp3 file named: `Artist - Title.mp3`

# Usage
## Downloading MP3 from YouTube URL
Create trimmed, normalized, tagged mp3:
```shell
trimmer url https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Editing MP3
Trim down manually (e.g. long applause at the end of song)
```shell
trimmer mp3 "Rick Astley - Never Gonna Give You Up.mp3" --trim-end 30
```

## Help
```shell
trimmer --help
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
- full readme/docs, sublog screen
- extracting artist - title from youtube-dl title
- idempotent trimming (not trimming fade-outs again)
- fix sublog real traceback for wrapped exception
