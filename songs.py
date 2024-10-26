# Usage: python3 hello.py song [artist]
# python3 hello.py "Ma ucide ea" "Mihail"
# python3 hello.py "nu te mai astept" "alina eremia"

# Idea:
# - Fetch lyrics from genius.com
# - Translate to English
# - Display original and English translated lyrics side-by-side

import argparse, os
from dotenv import load_dotenv
from side_by_side import print_side_by_side

# Class to get song lyrics from Genius
from fetch_lyrics import FetchLyrics
# Class to translate lyrics using Microsoft Azure AI Translator
from translate_lyrics import TranslateLyrics

# loading variables from .env file
load_dotenv()

#
# Parse arguments
#

parser = argparse.ArgumentParser()
parser.add_argument("song", nargs="+")
args = parser.parse_args()

song = args.song[0]
artist = args.song[1] if len(args.song) > 1 else None

#
# Fetch song lyrics
#

lyrics_fetcher = FetchLyrics(os.getenv("GENIUS_ACCESS_TOKEN"))
song_lyrics = lyrics_fetcher.fetch_lyrics(song, artist)

#
# Translate lyrics to English
#

lyrics_translator = TranslateLyrics(os.getenv("MS_TRANSLATOR_KEY"))
english_translation = lyrics_translator.translate_lyrics(song_lyrics)

#
# Display original and English translated lyrics side-by-side
#
print()
print_side_by_side("Original:", "English:")
print_side_by_side("=========", "========")
print()
print_side_by_side(song_lyrics, english_translation)
print()
