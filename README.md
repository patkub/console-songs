# console-songs
Display song lyrics in console

### Requirements
A `.env` file with:
```
GENIUS_ACCESS_TOKEN=your_api_token_here...
```
[Genius API](https://docs.genius.com)

### Usage

Provide the song and optionally the artist's name
```
python3 hello.py song [artist]
```

Example:
```
python3 hello.py "Ma ucide ea" "Mihail"
```

### Sample Output
```
(console-songs) patka@Patricks-MacBook-Air console-songs % python3 hello.py "Ma ucide ea" "Mihail"
Looking for song Ma ucide ea by artist Mihail
Searching for "Ma ucide ea" by Mihail...
Done.

Lyrics:
7 ContributorsMă ucide ea Lyrics[Strofa 1]
E totul în viteză
Delir cât cerul de înalt
Suntem în antiteză
Subiecții unui simplu joc murdar
...
```