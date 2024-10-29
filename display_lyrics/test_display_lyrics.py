from .BaseDisplayLyrics import BaseDisplayLyrics
from .ConsoleDisplayLyrics import ConsoleDisplayLyrics
from unittest.mock import patch, call


def test_display_lyrics_obj():
    """
    Instantiates ConsoleDisplayLyrics
    """
    display_lyrics = ConsoleDisplayLyrics()
    assert isinstance(display_lyrics, ConsoleDisplayLyrics)


def fake_print_side_by_side(output1, output2):
    pass


def get_expected_print_calls(song_info):
    """
    Expect to print: title, url, and two blank lines
    @param song_info: song_info object
    """
    # expect to print: title, url, and two blank lines
    expected_print_calls = [
        call("\n{}".format(song_info.full_title)),
        call("{}\n".format(song_info.url)),
        call(),
        call(),
    ]
    return expected_print_calls


@patch("builtins.print")
@patch("side_by_side.print_side_by_side", fake_print_side_by_side)
def test_display_lyrics_method(mocked_print):
    """
    Displays original and English translated lyrics side-by-side
    """

    class FakeSongInfo:
        pass

    # mock a fake song_info object
    song_info = FakeSongInfo()
    song_info.full_title = "full title"
    song_info.url = "https://example.com/"

    # instantiate and display lyrics
    display_lyrics = ConsoleDisplayLyrics()
    display_lyrics.display_lyrics(song_info, "original", "english")

    # assert
    assert isinstance(display_lyrics, BaseDisplayLyrics)
    # expect to print: title, url, and two blank lines
    expected_print_calls = get_expected_print_calls(song_info)
    mocked_print.assert_has_calls(expected_print_calls)


@patch("builtins.print")
@patch("side_by_side.print_side_by_side", fake_print_side_by_side)
def test_display_lyrics_method_original_longer(mocked_print):
    """
    Displays original and English translated lyrics side-by-side
    Original text longer than translated
    """

    class FakeSongInfo:
        pass

    # mock a fake song_info object
    song_info = FakeSongInfo()
    song_info.full_title = "full title"
    song_info.url = "https://example.com/"

    # instantiate and display lyrics
    display_lyrics = ConsoleDisplayLyrics()
    display_lyrics.display_lyrics(song_info, "original\n\ntext\n\nlonger", "english")

    # assert
    assert isinstance(display_lyrics, BaseDisplayLyrics)
    # expect to print: title, url, and two blank lines
    expected_print_calls = get_expected_print_calls(song_info)
    mocked_print.assert_has_calls(expected_print_calls)


@patch("builtins.print")
@patch("side_by_side.print_side_by_side", fake_print_side_by_side)
def test_display_lyrics_method_original_shorter(mocked_print):
    """
    Displays original and English translated lyrics side-by-side
    Original text shorter than translated
    """

    class FakeSongInfo:
        pass

    # mock a fake song_info object
    song_info = FakeSongInfo()
    song_info.full_title = "full title"
    song_info.url = "https://example.com/"

    # instantiate and display lyrics
    display_lyrics = ConsoleDisplayLyrics()
    display_lyrics.display_lyrics(song_info, "original", "english\n\ntext\n\nlonger")

    # assert
    assert isinstance(display_lyrics, BaseDisplayLyrics)
    # expect to print: title, url, and two blank lines
    expected_print_calls = get_expected_print_calls(song_info)
    mocked_print.assert_has_calls(expected_print_calls)
