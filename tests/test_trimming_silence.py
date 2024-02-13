from pydub import AudioSegment

from trimmer.normalizer import detect_leading_silence


def test_trim_down_the_silence():
    song = AudioSegment.from_mp3("./tests/tubular_ex.mp3")

    start_trim = detect_leading_silence(song)
    end_trim = detect_leading_silence(song.reverse())

    trimmed_song = song[start_trim:-end_trim]

    trimmed_song.export("./tests/result_tubular_trimmed.mp3", format="mp3")
    trimmed_song = AudioSegment.from_mp3("./tests/result_tubular_trimmed.mp3")
    duration_s = len(trimmed_song) / 1000
    assert 76 < duration_s < 77
