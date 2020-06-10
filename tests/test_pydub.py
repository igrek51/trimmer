from pydub import AudioSegment

from trimmer.mp3_normalizer import detect_leading_silence


def test_volume_normalize():
    song = AudioSegment.from_mp3("./tests/tubular_ex.mp3")

    gain = -song.max_dBFS
    assert 3 < gain < 4

    normalized_song = song.apply_gain(gain)
    normalized_song.export("./tests/result_tubular_normalized.mp3", format="mp3")

    normalized_song = AudioSegment.from_mp3("./tests/result_tubular_normalized.mp3")
    assert -0.6 < normalized_song.max_dBFS < 0.6


def test_trim_down_the_silence():
    song = AudioSegment.from_mp3("./tests/tubular_ex.mp3")

    start_trim = detect_leading_silence(song)
    end_trim = detect_leading_silence(song.reverse())

    duration = len(song)
    trimmed_song = song[start_trim:duration - end_trim]

    trimmed_song.export("./tests/result_tubular_trimmed.mp3", format="mp3")
    trimmed_song = AudioSegment.from_mp3("./tests/result_tubular_trimmed.mp3")
    duration_s = len(trimmed_song) / 1000
    assert 76 < duration_s < 77


def test_fade_out():
    song = AudioSegment.from_mp3("./tests/tubular.mp3")
    faded_song = song.fade_in(500).fade_out(2000)
    faded_song.export("./tests/result_tubular_faded.mp3", format="mp3")
