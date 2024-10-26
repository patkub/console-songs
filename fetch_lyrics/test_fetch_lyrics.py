from .FetchLyrics import FetchLyrics
from unittest.mock import patch


@patch('lyricsgenius.Genius.search_song')
def test_fetch_lyrics_calls_genius_api(mock_search_song):
    """
    Fetches lyrics for a song given its name and artist by calling Genius API
    Mocks underlying call to lyricsgenius.Genius.search_song and asserts it was called
    """

    # Prepare: instantiate FetchLyrics with fake access token
    access_token = "fake_access_token"
    fetch_lyrics = FetchLyrics(access_token)

    # Act: fetch lyrics for a fake song and artist
    # underlying lyricsgenius.Genius.search_song is mocked
    fetch_lyrics.fetch_lyrics("fake_song", "fake_artist")

    # Assert underlying mocked lyricsgenius.Genius.search_song was called
    mock_search_song.assert_called_with("fake_song", "fake_artist")

