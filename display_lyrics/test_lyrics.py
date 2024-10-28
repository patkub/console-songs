from .Lyrics import Lyrics


def test_lyrics_obj():
    """
    Instantiates Lyrics
    """
    lyrics_obj = Lyrics("some\n\nlyrics")
    assert isinstance(lyrics_obj, Lyrics)


def test_lyrics():
    """
    Test lyrics
    """

    # Prepare
    lyrics_text = "some\n\nlyrics"
    expected_stanzas = ["some", "lyrics"]

    # Act
    lyrics_obj = Lyrics(lyrics_text)

    # Assert
    assert isinstance(lyrics_obj, Lyrics)
    assert lyrics_obj.get_lyrics() == lyrics_text
    assert lyrics_obj.get_stanzas() == expected_stanzas
    assert lyrics_obj.get_num_stanzas() == len(expected_stanzas)


def test_min_stanzas():
    """
    Gets the minimum number of stanzas between two lyrics
    """

    # Prepare
    text_two = "one\n\ntwo"
    text_three = "one\n\ntwo\n\nthree"

    # Act
    lyrics1 = Lyrics(text_two)
    lyrics2 = Lyrics(text_three)
    min_stanzas = lyrics1.get_min_stanzas(lyrics2)

    # Assert
    assert min_stanzas == 2


def test_update_lyrics():
    """
    Test updating lyrics
    """

    # Prepare
    lyrics_old_text = "some\n\nlyrics"

    lyrics_new_text = "these\n\nare\n\nthe\n\nnew\n\nlyrics"
    expected_new_stanzas = ["these", "are", "the", "new", "lyrics"]

    # Act
    lyrics_obj = Lyrics(lyrics_old_text)
    lyrics_obj.set_lyrics(lyrics_new_text)

    # Assert
    assert isinstance(lyrics_obj, Lyrics)
    assert lyrics_obj.get_lyrics() == lyrics_new_text
    assert lyrics_obj.get_stanzas() == expected_new_stanzas
    assert lyrics_obj.get_num_stanzas() == len(expected_new_stanzas)
