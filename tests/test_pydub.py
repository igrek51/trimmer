from pydub import AudioSegment


def test_volume_normalize():
    song = AudioSegment.from_mp3("./tests/tubular_ex.mp3")

    gain = -song.max_dBFS
    assert 3 < gain < 4

    normalized_song = song.apply_gain(gain)
    normalized_song.export("./tests/result_tubular_normalized.mp3", format="mp3")

    normalized_song = AudioSegment.from_mp3("./tests/result_tubular_normalized.mp3")
    assert -0.6 < normalized_song.max_dBFS < 0.6


def test_fade_out():
    song = AudioSegment.from_mp3("./tests/tubular.mp3")
    faded_song = song.fade_in(500).fade_out(2000)
    faded_song.export("./tests/result_tubular_faded.mp3", format="mp3")
