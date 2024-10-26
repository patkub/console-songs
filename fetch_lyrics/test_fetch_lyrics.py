from lyricsgenius import Genius
from .FetchLyrics import FetchLyrics

def test_fetch_lyrics():
    access_token = "fake_access_token"
    fetch_lyrics = FetchLyrics(access_token)
    assert isinstance(fetch_lyrics.genius, Genius)
