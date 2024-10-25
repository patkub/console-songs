# Usage: python3 hello.py song [artist]
# python3 hello.py "Ma ucide ea" "Mihail"
# python3 hello.py "nu te mai astept" "alina eremia"

# Idea:
# - Fetch lyrics from genius.com
# - Translate to English
# - Display Romanian and English subtitles for song side-by-side

import argparse, os, uuid, requests
from dotenv import load_dotenv
from lyricsgenius import Genius
from side_by_side import print_side_by_side

def fetch_lyrics(song, artist):
    """
    Fetches lyrics for a song given name and artist

    If the argument `sound` isn't passed in, the default Animal
    sound is used.

    Parameters
    ----------
    song : str
        The name of the song

    artist : str
        The song's artist (Default is None)

    Raises
    ------
    NotImplementedError
        If no sound is set for the animal or passed in as a
        parameter.
    """
    print("Looking for song {} by artist {}".format(song, artist))

    # Genius API
    genius = Genius(os.getenv("GENIUS_ACCESS_TOKEN"))
    # https://genius.com/Mihail-ma-ucide-ea-lyrics
    song = genius.search_song(song, artist)

    return song.lyrics


# loading variables from .env file
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("song", nargs="+")
args = parser.parse_args()

song = args.song[0]
artist = args.song[1] if len(args.song) > 1 else None


# Fetch lyrics for song
song_lyrics = fetch_lyrics(song, artist)
print("\nLyrics:")
# print(song_lyrics)
# line-by-line split of the lyrics
#lyrics_lines = song.lyrics.split("\n")
# print(lyrics_lines)



# Translate Romanian to English
subscription_key=os.getenv("MS_TRANSLATOR_KEY")

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
endpoint = "https://api.cognitive.microsofttranslator.com/"
path = '/translate?api-version=3.0'
# from romanian to english
params = '&from=ro&to=en'
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': 'eastus',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text' : song_lyrics
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()
#print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))

english_translation = response[0]["translations"][0]["text"]

print_side_by_side(song_lyrics, english_translation)
