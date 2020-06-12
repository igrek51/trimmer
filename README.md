# Trimmer
Songs downloader & normalizer for automatic MP3 processing, which:

1. Downloads mp3 from given youtube URL (thanks to youtube-dl)
2. Trims down silence at the beginning & at the end of song (thanks to pydub)
3. Normalizes volume level, applies fade-in & fade-out (thanks to pydub)
4. Adds MP3 ID3v2 tags (thanks to eyed3)
5. Creates mp3 file named: `Artist - Title.mp3`

# Installation


## Install locally
```shell
./setup_venv.sh
. venv/bin/activate
python setup.py develop
```

# Usage

# TODO
- full readme/docs
- extracting artis - title from youtube-dl title
- idempotent trimming (not trimming fade-outs again)
- fix sublog real traceback for wrapped exception
