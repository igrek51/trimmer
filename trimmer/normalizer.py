import os
from typing import Optional

from nuclear.sublog import wrap_context, log
from pydub import AudioSegment


def normalize_song(mp3_file: str, no_trim: bool, no_fade: bool, no_normalize: bool,
                   user_trim_start: Optional[float] = None, user_trim_end: Optional[float] = None,
                   user_gain: Optional[float] = None):
    with wrap_context('normalizing mp3', mp3_file=mp3_file):
        log.info('loading song...', mp3_file=mp3_file)
        song = AudioSegment.from_mp3(mp3_file)

        if not no_normalize:
            if user_gain is not None:
                gain = user_gain
            else:
                volume = calculate_volume(song)
                log.info('normalizing volume level...', volume=f'{volume:.2f}dB', dBFS=f'{song.dBFS:.2f}dB')
                gain = -volume
            song = song.apply_gain(gain)
            log.info('volume normalized', gain=f'{gain:.2f}dB')

        if not no_trim:
            log.info('trimming silence...')
            start_trim = user_trim_start * 1000 if user_trim_start is not None else detect_leading_silence(song)
            end_trim = user_trim_end * 1000 if user_trim_end is not None else detect_leading_silence(song.reverse(),
                                                                                                     margin=0)
            pre_duration = len(song)
            song = song[start_trim:len(song) - end_trim]
            post_duration = len(song)
            log.info('silence trimmed', trim_start=duration_to_human(start_trim), trim_end=duration_to_human(end_trim),
                     duration_before=duration_to_human(pre_duration), duration_after=duration_to_human(post_duration))

        if not no_fade:
            fade_in_duration = 100
            fade_out_duration = 1000
            log.info('applying fade-in & fade-out...',
                     fade_in=duration_to_human(fade_in_duration), fade_out=duration_to_human(fade_out_duration))
            song = song.fade_in(fade_in_duration).fade_out(fade_out_duration)

        duartion = len(song)
        log.info('saving song...', mp3_file=mp3_file, duration=duration_to_human(duartion))
        song.export(mp3_file, format="mp3")


def calculate_volume(song: AudioSegment) -> float:
    volume = song.max_dBFS
    if volume < -0.1:
        return volume

    lower_vol = 10
    tmp_clip = '.anti_clip.mp3'
    log.debug('detecting clipping...')
    lowered = song.apply_gain(-lower_vol)
    lowered.export(tmp_clip, format="mp3")
    lowered = AudioSegment.from_mp3(tmp_clip)
    os.remove(tmp_clip)
    return lowered.max_dBFS + lower_vol


def detect_leading_silence(song: AudioSegment, margin: int = 100) -> int:
    silence_threshold = -45.0  # dB
    trim_ms = 0  # ms
    chunk_size = 50  # ms

    while song[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(song):
        trim_ms += chunk_size

    if trim_ms >= margin:
        return trim_ms - margin
    return trim_ms


def duration_to_human(ms: int) -> str:
    sec = ms / 1000
    if sec < 60:
        return f'{sec:.3f}s'
    minutes = int(sec // 60)
    sec = sec % 60
    return f'{minutes}:{sec:06.3f}'
