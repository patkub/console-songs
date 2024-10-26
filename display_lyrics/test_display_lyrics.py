from .DisplayLyrics import DisplayLyrics
from mock import patch, call


def test_display_lyrics():
    """
    Instantiates DisplayLyrics
    """
    display_lyrics = DisplayLyrics()
    assert isinstance(display_lyrics, DisplayLyrics)


def fake_print_side_by_side(output1, output2):
    pass


@patch('builtins.print')
@patch('side_by_side.print_side_by_side', fake_print_side_by_side)
def test_display_lyrics_method(mocked_print):
    """
    Instantiates DisplayLyrics
    """

    class FakeSongInfo:
        pass

    # mock a fake song_info object
    song_info = FakeSongInfo()
    song_info.full_title = "full title"
    song_info.url = "https://example.com/"

    # instantiate and display lyrics
    display_lyrics = DisplayLyrics()
    display_lyrics.display_lyrics(song_info, "original", "english")

    # expect to print: title, url, and two blank lines
    expected_print_calls = [
        call("\n{}".format(song_info.full_title)),
        call("{}\n".format(song_info.url)),
        call(),
        call()
    ]

    # assert
    assert isinstance(display_lyrics, DisplayLyrics)
    # assert print calls
    mocked_print.assert_has_calls(expected_print_calls)
