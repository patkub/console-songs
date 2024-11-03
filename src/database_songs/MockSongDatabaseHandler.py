class MockSongDatabaseHandler:  # pragma: no cover
    def __init__(self):
        self.con = None

    def setup_song_database(self):
        """
        Set up a database to store songs and their translations
        @return: database connection, or None if error occurred
        """
        return None

    def get_song_artist(self, name, artist):
        """
        Fetch song by name and artist from database
        @param name: song name
        @param artist: song artist
        @return: song, or None if not found
        """
        return None

    def search_song_by_name(self, name, artist):
        """
        Search for song by name and artist in database
        @param name: song name
        @param artist: artist name or None
        @return: song, or None if not found
        """
        return None

    def save_song(self, song_info, lyrics, translation):
        """
        Save song in database
        @param song_info: song info
        @param lyrics: original lyrics
        @param translation: English translation
        @return: True on success, False otherwise
        """
        return True
