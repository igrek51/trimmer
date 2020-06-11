from typing import Optional

from pydub import AudioSegment

from trimmer.sublog import wrap_context, info


def normalize_song(mp3_file: str, trim_start: Optional[float] = None, trim_end: Optional[float] = None):
    with wrap_context('normalizing mp3', mp3_file=mp3_file):
        info('loading song...', mp3_file=mp3_file)
        song = AudioSegment.from_mp3(mp3_file)

        info('normalizing volume level...')
        gain = -song.max_dBFS
        song = song.apply_gain(gain)
        info('volume normalized', gain=f'{gain:.2f}dB')

        info('trimming silence...')
        if trim_start:
            trim_start = trim_start * 1000
        if trim_end:
            trim_end = trim_end * 1000
        start_trim = trim_start or detect_leading_silence(song)
        end_trim = trim_end or detect_leading_silence(song.reverse(), margin=0)
        pre_duration = len(song)
        song = song[start_trim:-end_trim]
        post_duration = len(song)
        info('silence trimmed', trim_start=duration_to_human(start_trim), trim_end=duration_to_human(end_trim),
             duration_before=duration_to_human(pre_duration), duration_after=duration_to_human(post_duration))

        fade_in_duration = 100
        fade_out_duration = 1000
        info('applying fade-in & fade-out...',
             fade_in=duration_to_human(fade_in_duration), fade_out=duration_to_human(fade_out_duration))
        song = song.fade_in(fade_in_duration).fade_out(fade_out_duration)

        duartion = len(song)
        info('saving song...', mp3_file=mp3_file, duration=duration_to_human(duartion))
        song.export(mp3_file, format="mp3")


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
