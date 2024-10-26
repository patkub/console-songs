# console-songs

> Given a song and artist, fetches lyrics from [Genius](https://genius.com), translates them to English using [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/), and displays them side-by-side in the console.

[![Python package](https://github.com/patkub/console-songs/actions/workflows/python-app.yml/badge.svg)](https://github.com/patkub/console-songs/actions/workflows/python-app.yml)
![Python 3.x Required](https://img.shields.io/badge/python-3.x-brightgreen.svg)

### Requirements
A `.env` file with your API keys:
```
GENIUS_ACCESS_TOKEN=...
MS_TRANSLATOR_KEY=...
```
- [Genius API](https://docs.genius.com)
- [Azure Translator Resource](https://learn.microsoft.com/en-us/azure/ai-services/translator/create-translator-resource)

### Usage

Provide the song and optionally the artist's name
```
python3 songs.py song [artist]
```

Example:
```
python3 songs.py "Ma ucide ea" "Mihail"
```

### Sample Output
```
(console-songs) patka@Patricks-MacBook-Air console-songs % python3 songs.py "Ma ucide ea" "Mihail"
Looking for song Ma ucide ea by artist Mihail
Searching for "Ma ucide ea" by Mihail...
Done.

Mă ucide ea by Mihail
https://genius.com/Mihail-ma-ucide-ea-lyrics

Original:                                                                         English:
=========                                                                         ========

7 ContributorsMă ucide ea Lyrics[Strofa 1]                                        7 ContributorsShe Kills Me Lyrics[Verse 1]
E totul în viteză                                                                 It's all in speed
Delir cât cerul de înalt                                                          Delirium as high as the sky
Suntem în antiteză                                                                We are in antithesis
Subiecții unui simplu joc murdar                                                  The subjects of a simple dirty game
[Pre-refren]                                                                      [Pre-Chorus]
Ochii mei, rușinați, coboară doritor                                              My eyes, ashamed, descend willingly
...
```

### Unit Tests

Run unit tests with [pytest](https://docs.pytest.org/en/stable/) and report coverage.
```
pytest
```
