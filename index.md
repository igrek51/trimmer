---
hide:
  - navigation
---

# Trimmer
MP3 song normalizer

[![GitHub version](https://badge.fury.io/gh/igrek51%2Ftrimmer.svg)](https://github.com/igrek51/trimmer)
[![PyPI version](https://badge.fury.io/py/trimmer.svg)](https://pypi.org/project/trimmer)
[![Github Pages](https://img.shields.io/badge/docs-github.io-blue)](https://igrek51.github.io/trimmer)
[![Build Status](https://travis-ci.org/igrek51/trimmer.svg?branch=master)](https://travis-ci.org/igrek51/trimmer)
[![codecov](https://codecov.io/gh/igrek51/trimmer/branch/master/graph/badge.svg)](https://codecov.io/gh/igrek51/trimmer)


Are you tired of quiet songs on Youtube with long silence before or after song? 

Trimmer does the following things:

1. Downloads songs from given Youtube URL (thanks to [youtube-dl](https://github.com/ytdl-org/youtube-dl))
2. Trims down silence at the beginning & at the end of song (thanks to [pydub](https://github.com/jiaaro/pydub))
3. Normalizes volume level (detecting clipping), applies fade-in & fade-out (thanks to [pydub](https://github.com/jiaaro/pydub))
4. Adds MP3 ID3 tags - both ID3v1 & ID3v2 (thanks to [eyed3](https://github.com/nicfit/eyeD3))
5. Creates mp3 file named: `Artist - Title.mp3`

## Downloading MP3
Create trimmed, normalized & tagged mp3 from Youtube URL:

<div class="termy">
```console
$ trimmer https://www.youtube.com/watch?v=dQw4w9WgXcQ
<span class="code-gray">[2023-03-06 23:08:27]</span> <span class="code-blue">INFO</span>  source recognized as url <span class="code-green">source=</span><span class="code-bold-green">https://www.youtube.com/watch?v=dQw4w9WgXcQ</span>
<span class="code-gray">[2023-03-06 23:08:27]</span> <span class="code-blue">INFO</span>  fetching metadata from youtube page... <span class="code-green">url=</span><span class="code-bold-green">https://www.youtube.com/watch?v=dQw4w9WgXcQ</span>
<span class="code-gray">[2023-03-06 23:08:31]</span> <span class="code-blue">INFO</span>  youtube page metadata fetched <span class="code-green">yt_title="</span><span class="code-bold-green">Rick Astley - Never Gonna Give You Up (Official Music Video)</span><span class="code-green">" artist=</span><span class="code-bold-green">None</span>
<span class="code-gray">[2023-03-06 23:08:31]</span> <span class="code-blue">INFO</span>  artist & title extracted from youtube page <span class="code-green">artist="</span><span class="code-bold-green">Rick Astley</span><span class="code-green">" title="</span><span class="code-bold-green">Never Gonna Give You Up</span><span class="code-green">"</span>
Enter Artist ("Rick Astley" by default): <span>Rick Astley</span>
Enter Title ("Never Gonna Give You Up" by default): <span>Never Gonna Give You Up</span>
<span class="code-gray">[2023-03-06 23:08:36]</span> <span class="code-blue">INFO</span>  song name set <span class="code-green">name="</span><span class="code-bold-green">Rick Astley - Never Gonna Give You Up</span><span class="code-green">"</span>
<span class="code-gray">[2023-03-06 23:08:36]</span> <span class="code-blue">INFO</span>  downloading from youtube... <span class="code-green">url=</span><span class="code-bold-green">https://www.youtube.com/watch?v=dQw4w9WgXcQ</span>
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  song downloaded <span class="code-green">tmpfile=</span><span class="code-bold-green">trimmer_dl_b737b09b-beb7-412e-901a-425e14418b5c.mp3</span>
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  song renamed <span class="code-green">new_name="</span><span class="code-bold-green">Rick Astley - Never Gonna Give You Up.mp3</span><span class="code-green">"</span>
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  loading song...
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  normalizing volume level... <span class="code-green">volume=</span><span class="code-bold-green">-0.98dB</span> <span class="code-green">dBFS=</span><span class="code-bold-green">-16.97dB</span>
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  volume normalized <span class="code-green">gain=</span><span class="code-bold-green">0.98dB</span>
<span class="code-gray">[2023-03-06 23:08:42]</span> <span class="code-blue">INFO</span>  trimming silence...
<span class="code-gray">[2023-03-06 23:08:43]</span> <span class="code-blue">INFO</span>  silence trimmed <span class="code-green">trim_start=</span><span class="code-bold-green">0.000s</span> <span class="code-green">trim_end=</span><span class="code-bold-green">2.000s</span> <span class="code-green">duration_before=</span><span class="code-bold-green">3:32.045</span> <span class="code-green">duration_after=</span><span class="code-bold-green">3:30.045</span>
<span class="code-gray">[2023-03-06 23:08:43]</span> <span class="code-blue">INFO</span>  applying fade-in & fade-out... <span class="code-green">fade_in=</span><span class="code-bold-green">0.100s</span> <span class="code-green">fade_out=</span><span class="code-bold-green">1.000s</span>
<span class="code-gray">[2023-03-06 23:08:43]</span> <span class="code-blue">INFO</span>  saving song... <span class="code-green">mp3_file="</span><span class="code-bold-green">Rick Astley - Never Gonna Give You Up.mp3</span><span class="code-green">" duration=</span><span class="code-bold-green">3:30.045</span>
<span class="code-gray">[2023-03-06 23:08:46]</span> <span class="code-blue">INFO</span>  tagging mp3... <span class="code-green">artist="</span><span class="code-bold-green">Rick Astley</span><span class="code-green">" title="</span><span class="code-bold-green">Never Gonna Give You Up</span><span class="code-green">"</span>
<span class="code-gray">[2023-03-06 23:08:46]</span> <span class="code-blue">INFO</span>  song saved <span class="code-green">mp3_file="</span><span class="code-bold-green">Rick Astley - Never Gonna Give You Up.mp3</span><span class="code-green">"</span>
```

</div>

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
