from lyricsgenius import Genius


class FetchLyrics:
    def __init__(self, access_token):
        """
        Get song lyrics from Genius.
        @param access_token: string access token for Genius API https://docs.genius.com
        """
        self.genius = Genius(access_token)

    def fetch_lyrics(self, song, artist):
        """
        Fetches lyrics for a song given its name and artist

        @param song: string song name
        @param artist: string artist name
        @return: string song lyrics
        """

        print("Looking for song {} by artist {}".format(song, artist))
        # https://genius.com/Mihail-ma-ucide-ea-lyrics
        song = self.genius.search_song(song, artist)

        return song.lyrics
