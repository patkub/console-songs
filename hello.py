# Usage: python3 hello.py song [artist]
# python3 hello.py "Ma ucide ea" "Mihail"
# python3 hello.py "nu te mai astept" "alina eremia"

# Idea:
# - fetch lyrics from genius.com
# - translate to English
# - display Romanian and English subtitles for song side-by-side

# TODO: Romanian to English translation

import argparse, os
from dotenv import load_dotenv, dotenv_values
from lyricsgenius import Genius
from side_by_side import print_side_by_side

# loading variables from .env file
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("song", nargs="+")
args = parser.parse_args()

song = args.song[0]
artist = args.song[1] if len(args.song) > 1 else None

print("Looking for song {} by artist {}".format(song, artist))

# Genius API
genius = Genius(os.getenv("GENIUS_ACCESS_TOKEN"))
# https://genius.com/Mihail-ma-ucide-ea-lyrics
song = genius.search_song(song, artist)

print("\nLyrics:")
#print(song.lyrics)

# line-by-line split of the lyrics
lyrics_lines = song.lyrics.split("\n")
#print(lyrics_lines)



# Translate Romanian to English
# TODO:...

# TODO: eventually replace the right side with English translation
print_side_by_side(song.lyrics, song.lyrics)
