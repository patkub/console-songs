import re


class Lyrics:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.stanzas = []
        self.normalize_lyrics(lyrics)

    def normalize_lyrics(self, lyrics):
        # normalize line endings
        self.lyrics = re.sub(r"[\r\n][\r\n]{2,}", "\n\n", lyrics)
        # split into stanzas
        self.stanzas = self.lyrics.split("\n\n")

    def get_lyrics(self):
        """
        Get the lyrics
        @return lyrics
        """
        return self.lyrics

    def set_lyrics(self, lyrics):
        """
        Set the lyrics. Normalizes and updates the stanzas
        @param lyrics new lyrics
        """
        self.normalize_lyrics(lyrics)

    def get_stanzas(self):
        """
        Get the stanzas
        """
        return self.stanzas
