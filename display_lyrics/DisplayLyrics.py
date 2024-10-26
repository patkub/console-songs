from side_by_side import print_side_by_side


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
        # Display song info
        print("\n{}".format(song_info.full_title))
        print("{}\n".format(song_info.url))
        # Display original and English translated lyrics side-by-side
        print_side_by_side("Original:", "English:")
        print_side_by_side("=========", "========")
        print()
        print_side_by_side(original_lyrics, english_lyrics)
        print()

