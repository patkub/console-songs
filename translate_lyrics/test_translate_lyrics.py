from .TranslateLyrics import TranslateLyrics


def test_translate_lyrics_sets_translator_key():
    """
    Sets translator key
    """
    translator_key = "fake_translator_key"
    translate_lyrics = TranslateLyrics(translator_key)
    assert translate_lyrics.subscription_key == translator_key
