import eyed3
from eyed3.id3 import ID3_V2_4, ID3_V1_1
from pydub import AudioSegment


def test_export_id3_tags():
    song = AudioSegment.from_mp3("./tests/tubular.mp3")
    song.export("./tests/result_tubular_tags.mp3", format="mp3")

    audiofile = eyed3.load("./tests/result_tubular_tags.mp3")
    audiofile.tag.artist = "Artistążół"
    audiofile.tag.title = "I'm a pickle ążśółć too long title to be displayed"

    audiofile.tag.save(version=ID3_V2_4)
    audiofile.tag.save(version=ID3_V1_1)
