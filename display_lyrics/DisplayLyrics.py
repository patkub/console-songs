import side_by_side
from .Lyrics import Lyrics


class DisplayLyrics:
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

        # minimum set of stanzas between two lyrics
        min_stanzas = original_lyrics_obj.get_min_stanzas(english_lyrics_obj)

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

        # Display portion that has both original and english translation
        for i in range(min_stanzas):
            side_by_side.print_side_by_side(
                split_original_lyrics[i], split_english_lyrics[i]
            )
            print()

        if len_original_lyrics > len_english_lyrics:
            # original lyrics have more than english translation
            for i in range(len_original_lyrics - min_stanzas):
                side_by_side.print_side_by_side(
                    split_original_lyrics[min_stanzas - 1 + i], ""
                )
                print()
        elif len_english_lyrics > len_original_lyrics:
            # english translated lyrics have more than original
            for i in range(len_english_lyrics - min_stanzas):
                side_by_side.print_side_by_side(
                    "", split_english_lyrics[min_stanzas - 1 + i]
                )
                print()
