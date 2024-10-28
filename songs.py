# Usage: python3 songs.py song [artist]
# python3 songs.py "Ma ucide ea" "Mihail"
# python3 songs.py "nu te mai astept" "alina eremia"

# Idea:
# - Fetch song lyrics from genius.com
# - Translate to English
# - Display original and English translated lyrics side-by-side

import argparse, os
from dotenv import load_dotenv

# Class to get song lyrics from Genius
from fetch_lyrics import FetchLyrics, PatchedGenius
# Class to translate lyrics using Microsoft Azure AI Translator
from translate_lyrics import TranslateLyrics
# Display output
from display_lyrics import DisplayLyrics

# loading variables from .env file
load_dotenv()


def process_song(song, artist, access_keys, genius_patch):
    """
    Fetch song lyrics, translate to English, and display original and English side-by-side lyrics.
    @param song: the name of the song
    @param artist: the name of the artist
    @param access_keys: dictionary of API access keys
    @param genius_patch: use patched version of Genius api
    """
    #
    # Fetch song lyrics from Genius
    #
    patched_genius = PatchedGenius if genius_patch else None
    lyrics_fetcher = FetchLyrics(access_keys["GENIUS_ACCESS_TOKEN"], patched_genius)
    song_info = lyrics_fetcher.fetch_lyrics(song, artist)
    if song_info is None:
        # song not found, end
        return

    song_lyrics = song_info.lyrics

    #
    # Translate lyrics to English using Microsoft Azure AI Translator
    #
    lyrics_translator = TranslateLyrics(access_keys["MS_TRANSLATOR_KEY"], access_keys["MS_TRANSLATOR_REGION"])
    english_translation = lyrics_translator.translate_lyrics(song_lyrics)

    #
    # Display original and English translated lyrics side-by-side
    #
    DisplayLyrics.display_lyrics(song_info, song_lyrics, english_translation)


if __name__ == '__main__':  # pragma: no cover
    #
    # Parse arguments
    #

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("song", nargs="+")
    parser.add_argument('--genius-patch',
                        action=argparse.BooleanOptionalAction,
                        default=True,
                        help='Use patched version of Genius API')
    args = parser.parse_args()

    song = args.song[0]
    artist = args.song[1] if len(args.song) > 1 else None

    access_keys = {
        'GENIUS_ACCESS_TOKEN': os.getenv("GENIUS_ACCESS_TOKEN"),
        'MS_TRANSLATOR_KEY': os.getenv("MS_TRANSLATOR_KEY"),
        'MS_TRANSLATOR_REGION': os.getenv("MS_TRANSLATOR_REGION")
    }

    #
    # Fetch song lyrics, translate to English, and display original and English side-by-side lyrics.
    #

    process_song(song, artist, access_keys, args.genius_patch)
