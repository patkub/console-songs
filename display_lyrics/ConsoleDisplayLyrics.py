import side_by_side
from .BaseDisplayLyrics import BaseDisplayLyrics
from .Lyrics import Lyrics


class ConsoleDisplayLyrics(BaseDisplayLyrics):
    def __init__(self):
        """
        Display original and English translated lyrics side-by-side
        """

    @staticmethod
    def display_lyrics(song_info, original_lyrics, english_lyrics):
        """
        Display original and English translated lyrics side-by-side
        @param song_info: song object from Genius API https://docs.genius.com
        @param original_lyrics: string original lyrics
        @param english_lyrics: string English translation
        """

        # Process the lyrics
        original_lyrics_obj = Lyrics(original_lyrics)
        english_lyrics_obj = Lyrics(english_lyrics)

        split_original_lyrics = original_lyrics_obj.get_stanzas()
        split_english_lyrics = english_lyrics_obj.get_stanzas()

        len_original_lyrics = len(split_original_lyrics)
        len_english_lyrics = len(split_english_lyrics)

        # Display song info
        print("\n{}".format(song_info.full_title))
        print("{}\n".format(song_info.url))

        # Display original and English translated lyrics side-by-side
        side_by_side.print_side_by_side("Original:", "English:")
        side_by_side.print_side_by_side("=========", "========")
        print()
        # Display original and English translated lyrics side-by-side
        for i in range(max(len_original_lyrics, len_english_lyrics)):
            # empty string on the side that has less
            side_by_side.print_side_by_side(
                split_original_lyrics[i] if len(split_original_lyrics) > i else "",
                split_english_lyrics[i] if len(split_english_lyrics) > i else "",
            )
            # line breaks between stanzas
            print()
