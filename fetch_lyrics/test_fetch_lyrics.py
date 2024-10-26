from lyricsgenius import Genius
from .FetchLyrics import FetchLyrics


def test_fetch_lyrics_genius_obj():
    """
    Instantiates Genius api
    """
    access_token = "fake_access_token"
    fetch_lyrics = FetchLyrics(access_token)
    assert isinstance(fetch_lyrics.genius, Genius)
