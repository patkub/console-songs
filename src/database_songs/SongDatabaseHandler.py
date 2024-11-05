import os, sqlite3, sys


class SongDatabaseHandler:  # pragma: no cover
    def __init__(self):
        self.con = None

    def setup_song_database(self):
        """
        Set up a database to store songs and their translations
        @return: database connection, or None if error occurred
        """
        try:
            # create database of songs in script directory
            __dirname = os.path.dirname(sys.argv[0])
            con = sqlite3.connect(os.path.join(__dirname, "database_songs.db"))
            cur = con.cursor()
            cur.execute(
                """CREATE TABLE IF NOT EXISTS songs (
                        full_title TEXT,
                        artist TEXT,
                        url TEXT,
                        original_lyrics TEXT,
                        english_lyrics TEXT,
                        PRIMARY KEY(full_title, artist)
                    );"""
            )
            con.commit()
            self.con = con
            return con
        except sqlite3.Error:
            pass
        return None

    def get_song_artist(self, name, artist):
        """
        Fetch song by name and artist from database
        @param name: song name
        @param artist: song artist
        @return: song, or None if not found
        """
        try:
            if self.con:
                cur = self.con.cursor()
                res = cur.execute(
                    "SELECT * FROM songs WHERE full_title=? AND artist=?",
                    (name, artist),
                )
                if res:
                    return res.fetchone()
        except sqlite3.Error:
            pass
        return None

    def save_song(self, song_info, lyrics, translation):
        """
        Save song in database
        @param song_info: song info
        @param lyrics: original lyrics
        @param translation: English translation
        @return: True on success, False otherwise
        """
        # TODO: Update database to store multiple language translations for a single song
        success = True
        try:
            if self.con:
                cur = self.con.cursor()
                cur.execute(
                    """
                        INSERT INTO songs("full_title", "artist", "url", "original_lyrics", "english_lyrics") VALUES
                            (?, ?, ?, ?, ?)
                    """,
                    (
                        song_info.full_title,
                        song_info.artist,
                        song_info.url,
                        lyrics,
                        translation,
                    ),
                )
                self.con.commit()
        except sqlite3.Error:
            success = False
        return success
