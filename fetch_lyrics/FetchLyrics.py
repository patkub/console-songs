from lyricsgenius import Genius


class FetchLyrics:
    def __init__(self, access_token, custom_genius=None):
        """
        Get song lyrics from Genius.
        @param access_token: string access token for Genius API https://docs.genius.com
        @param custom_genius: optional custom Genius API object
        """

        # use custom Genius object if not null, otherwise default Genius object
        genius_obj = custom_genius if custom_genius is not None else Genius
        self.genius = genius_obj(access_token)

    def fetch_lyrics(self, song, artist):
        """
        Fetches lyrics for a song given its name and artist

        @param song: string song name
        @param artist: string artist name
        @return: object: song info
        """

        # print("Looking for song {} by artist {}".format(song, artist))
        # https://genius.com/Mihail-ma-ucide-ea-lyrics
        song = self.genius.search_song(song, artist)
        return song
