# Usage: python3 songs.py song [artist]
# python3 songs.py "Ma ucide ea" "Mihail"
# python3 songs.py "nu te mai astept" "alina eremia"

# Idea:
# - Fetch song lyrics from genius.com
# - Translate to English
# - Display original and English translated lyrics side-by-side

import argparse, os, sys
from dotenv import load_dotenv

# Class to get song lyrics from Genius
from fetch_lyrics import FetchLyrics, PatchedGenius
# Class to translate lyrics using Microsoft Azure AI Translator
from translate_lyrics import TranslateLyrics
# Display output
from display_lyrics import DisplayLyrics

# loading variables from .env file
load_dotenv()

#
# Parse arguments
#

parser = argparse.ArgumentParser()
parser.add_argument("song", nargs="+")
parser.add_argument('--experimental',
                    action=argparse.BooleanOptionalAction,
                    help='Enable experimental features.\nUses a patched version of Genius API')
args = parser.parse_args()

song = args.song[0]
artist = args.song[1] if len(args.song) > 1 else None

#
# Fetch song lyrics from Genius
#

patched_genius = PatchedGenius if args.experimental else None
lyrics_fetcher = FetchLyrics(os.getenv("GENIUS_ACCESS_TOKEN"), patched_genius)
song_info = lyrics_fetcher.fetch_lyrics(song, artist)
if song_info is None:
    # song not found
    sys.exit()

song_lyrics = song_info.lyrics

#
# Translate lyrics to English using Microsoft Azure AI Translator
#

lyrics_translator = TranslateLyrics(os.getenv("MS_TRANSLATOR_KEY"))
english_translation = lyrics_translator.translate_lyrics(song_lyrics)

#
# Display original and English translated lyrics side-by-side
#

DisplayLyrics.display_lyrics(song_info, song_lyrics, english_translation)
