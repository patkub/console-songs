from songs import process_song
from unittest.mock import Mock, patch, ANY

# mock object for reply from fetched lyrics
mockedFetchLyrics = Mock()
mockedFetchLyrics.lyrics = "mocked_lyrics"


@patch(
    "fetch_lyrics.FetchLyrics.FetchLyrics.fetch_lyrics", return_value=mockedFetchLyrics
)
@patch(
    "translate_lyrics.TranslateLyrics.TranslateLyrics.translate_lyrics",
    return_value="english translation",
)
@patch("display_lyrics.ConsoleDisplayLyrics.ConsoleDisplayLyrics.display_lyrics")
def test_process_song(
    mocked_display_lyrics, mocked_translate_lyrics, mocked_fetch_lyrics
):
    """
    Fetch song lyrics, translate to English, and display original and English side-by-side lyrics.
    """

    # Prepare
    song = "test_song_name"
    artist = "test_artist_name"
    access_keys = {
        "GENIUS_ACCESS_TOKEN": "fake_token_1",
        "MS_TRANSLATOR_KEY": "fake_token_2",
        "MS_TRANSLATOR_REGION": "fake_token_3",
    }
    experimental = False

    # Act
    process_song(song, artist, access_keys, experimental)

    # Assert
    # song searched by name and artist
    mocked_fetch_lyrics.assert_called_with(song, artist)
    # mocked lyrics get translated
    mocked_translate_lyrics.assert_called_with("mocked_lyrics")
    # display is called with song info, original and translated lyrics
    mocked_display_lyrics.assert_called_with(
        ANY, "mocked_lyrics", "english translation"
    )


@patch("fetch_lyrics.FetchLyrics.FetchLyrics.fetch_lyrics", return_value=None)
@patch(
    "translate_lyrics.TranslateLyrics.TranslateLyrics.translate_lyrics",
    return_value="english translation",
)
@patch("display_lyrics.ConsoleDisplayLyrics.ConsoleDisplayLyrics.display_lyrics")
def test_process_song_null(
    mocked_display_lyrics, mocked_translate_lyrics, mocked_fetch_lyrics
):
    """
    Null song fetched, translation and display are not called
    """

    # Prepare
    song = "test_song_name"
    artist = "test_artist_name"
    access_keys = {
        "GENIUS_ACCESS_TOKEN": "fake_token_1",
        "MS_TRANSLATOR_KEY": "fake_token_2",
        "MS_TRANSLATOR_REGION": "fake_token_3",
    }
    experimental = False

    # Act
    process_song(song, artist, access_keys, experimental)

    # Assert
    # song searched by name and artist
    mocked_fetch_lyrics.assert_called_with(song, artist)
    # fetched lyrics are null, so translation and display are not called
    mocked_translate_lyrics.assert_not_called()
    mocked_display_lyrics.assert_not_called()
