# Usage: python3 songs.py song [artist]
# python3 songs.py "Ma ucide ea" "Mihail"
# python3 songs.py "nu te mai astept" "alina eremia"

# Idea:
# - Fetch song lyrics from genius.com
# - Translate to English
# - Display original and English translated lyrics side-by-side

import argparse, os
from dotenv import load_dotenv

# Class to store songs
from database_songs import SongDatabaseHandler

# Class to get song lyrics from Genius
from fetch_lyrics import FetchLyrics, PatchedGenius

# Class to translate lyrics using Microsoft Azure AI Translator
from translate_lyrics import TranslateLyrics

# Display output
from display_lyrics import ConsoleDisplayLyrics

# loading variables from .env file
load_dotenv()


def process_song(song, artist, access_keys, refresh, genius_patch):
    """
    Fetch song lyrics, translate to English, and display original and English side-by-side lyrics.
    @param song: the name of the song
    @param artist: the name of the artist
    @param access_keys: dictionary of API access keys
    @param refresh: skip database and refresh song
    @param genius_patch: use patched version of Genius api
    """
    #
    # Fetch song lyrics from Genius
    #
    patched_genius = PatchedGenius if genius_patch else None
    lyrics_fetcher = FetchLyrics(access_keys["CS_GENIUS_ACCESS_TOKEN"], patched_genius)
    song_info = lyrics_fetcher.fetch_lyrics(song, artist)
    if song_info is None:
        # song not found, end
        return

    # get the song lyrics
    song_lyrics = song_info.lyrics

    #
    # Fetch song from database
    #
    song_db_handler = SongDatabaseHandler()
    song_db_con = song_db_handler.setup_song_database()
    if not refresh and song_db_con:  # pragma: no cover
        # fetch song from database
        song_res = song_db_handler.get_song_artist(
            song_info.full_title, song_info.artist
        )
        if song_res and len(song_res) >= 6:
            # already have this song saved in database
            english_translation = song_res[5]
            # display original and English translated lyrics side-by-side
            ConsoleDisplayLyrics.display_lyrics(
                song_info, song_lyrics, english_translation
            )
            # song fetched from database, end
            return

    #
    # Translate lyrics to English using Microsoft Azure AI Translator
    #
    lyrics_translator = TranslateLyrics(
        access_keys["CS_MS_TRANSLATOR_KEY"], access_keys["CS_MS_TRANSLATOR_REGION"]
    )
    english_translation = lyrics_translator.translate_lyrics(song_lyrics)

    # Save this song in the database
    song_db_handler.save_song(song_info, song_lyrics, english_translation)

    #
    # Display original and English translated lyrics side-by-side
    #
    ConsoleDisplayLyrics.display_lyrics(song_info, song_lyrics, english_translation)


def main():  # pragma: no cover
    #
    # Parse arguments
    #

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("song", nargs="+")
    parser.add_argument(
        "-r",
        "--refresh",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Skip database and refresh song",
    )
    parser.add_argument(
        "--genius-patch",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use patched version of Genius API",
    )
    args = parser.parse_args()

    song = args.song[0]
    artist = args.song[1] if len(args.song) > 1 else None

    access_keys = {
        "CS_GENIUS_ACCESS_TOKEN": os.getenv("CS_GENIUS_ACCESS_TOKEN"),
        "CS_MS_TRANSLATOR_KEY": os.getenv("CS_MS_TRANSLATOR_KEY"),
        "CS_MS_TRANSLATOR_REGION": os.getenv("CS_MS_TRANSLATOR_REGION"),
    }

    #
    # Fetch song lyrics, translate to English, and display original and English side-by-side lyrics.
    #

    process_song(song, artist, access_keys, args.refresh, args.genius_patch)


if __name__ == "__main__":  # pragma: no cover
    main()
