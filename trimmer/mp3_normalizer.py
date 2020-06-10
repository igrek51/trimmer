from pydub import AudioSegment

from trimmer.sublog import wrap_context, info


def detect_leading_silence(song, silence_threshold=-45.0, chunk_size=50):
    """
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    """
    trim_ms = 0  # ms
    assert chunk_size > 0
    while song[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(song):
        trim_ms += chunk_size
    return trim_ms


def ms_to_human_s(ms: int) -> str:
    sec = ms / 1000
    if sec < 60:
        return f'{sec}s'
    minutes = sec / 60
    sec = sec % 60
    return f'{minutes}m{sec}s'


def normalize_song(mp3_file: str):
    with wrap_context('normalizing mp3', mp3_file=mp3_file):
        info('loading song...', mp3_file=mp3_file)
        song = AudioSegment.from_mp3(mp3_file)

        info('normalizing volume level...')
        gain = -song.max_dBFS
        song = song.apply_gain(gain)
        info('volume normalized', gain=f'{gain}dB')

        info('trimming silence...')
        start_trim = detect_leading_silence(song)
        end_trim = detect_leading_silence(song.reverse())
        pre_duration = len(song)
        song = song[start_trim:pre_duration - end_trim]
        post_duration = len(song)
        info('silence trimmed', start_silence=ms_to_human_s(start_trim), end_silence=ms_to_human_s(end_trim),
             duration_before=ms_to_human_s(pre_duration), duration_after=ms_to_human_s(post_duration))

        fade_in_duration = 500
        fade_out_duration = 2000
        info('fading-in & fading-out...',
             fade_in=ms_to_human_s(fade_in_duration), fade_out=ms_to_human_s(fade_out_duration))
        song = song.fade_in(500).fade_out(2000)

        info('saving song...', mp3_file=mp3_file)
        song.export(mp3_file, format="mp3")
