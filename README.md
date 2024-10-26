# console-songs

> Given a song and artist, fetches lyrics from [Genius](https://genius.com), translates them to English using [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/), and displays original and translated lyrics side-by-side in the console.

[![Python package](https://github.com/patkub/console-songs/actions/workflows/python-app.yml/badge.svg)](https://github.com/patkub/console-songs/actions/workflows/python-app.yml)
![Python 3.x Required](https://img.shields.io/badge/python-3.x-brightgreen.svg)

### Idea
1. Fetch song lyrics
2. Translate to English
3. Display original and English translated lyrics side-by-side

Enjoy listening to music and learning a new language!

### Setup
Create an `.env` file with your API keys:
```
GENIUS_ACCESS_TOKEN=...
MS_TRANSLATOR_KEY=...
MS_TRANSLATOR_REGION=...
```
- [Genius API](https://docs.genius.com)
- [Azure Translator Resource](https://learn.microsoft.com/en-us/azure/ai-services/translator/create-translator-resource)

Setup a virtual environment:
```
python3 -m venv .
source bin/activate
```

Install dependencies:
```
pip3 install -r requirements.txt
```

You should now be able to run `python3 songs.py --help` and see usage.

### Usage

Provide the song and optionally the artist's name
```
python3 songs.py song [artist]
```
<details>

<summary>Full Usage</summary>

```
(console-songs) patka@Patricks-MacBook-Air console-songs % python3 songs.py --help
usage: songs.py [-h] [--experimental | --no-experimental] song [song ...]

positional arguments:
  song

options:
  -h, --help            show this help message and exit
  --experimental, --no-experimental
                        Enable experimental features. Uses a patched version of Genius API
```

</details>

Example:
```
python3 songs.py "Ma ucide ea" "Mihail"
```

### Sample Output
```
(console-songs) patka@Patricks-MacBook-Air console-songs % python3 songs.py "Ma ucide ea" "Mihail"
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

<details>

<summary>Full Output</summary>

```
(console-songs) patka@Patricks-MacBook-Air console-songs % python3 songs.py "Ma ucide ea" "Mihail"
Searching for "Ma ucide ea" by Mihail...
Done.

Mă ucide ea by Mihail
https://genius.com/Mihail-ma-ucide-ea-lyrics

Original:                                                                    English:                                                                   
=========                                                                    ========                                                                   

7 ContributorsMă ucide ea Lyrics[Strofa 1]                                   7 ContributorsShe Kills Me Lyrics[Verse 1]                                 
E totul în viteză                                                            It's all in speed                                                          
Delir cât cerul de înalt                                                     Delirium as high as the sky                                                
Suntem în antiteză                                                           We are in antithesis                                                       
Subiecții unui simplu joc murdar                                             The subjects of a simple dirty game                                        
[Pre-refren]                                                                 [Pre-Chorus]                                                               
Ochii mei, rușinați, coboară doritor                                         My eyes, ashamed, descend willingly                                        
Dar te respir, în acest urban decor                                          But I breathe you, in this urban setting                                   
[Refren]                                                                     [Chorus]                                                                   
Mă ucide ea, mă ucide ea                                                     She's killing me, she's killing me                                         
Încet...                                                                     Slow...                                                                    
Îmi vrea inima, îmi vrea inima                                               He wants my heart, he wants my heart                                       
Din piept                                                                    From the chest                                                             
[Strofa 2]                                                                   [Verse 2]                                                                  
E atât de grațioasă                                                          She's so graceful                                                          
Printre mulțimi de oameni                                                    Among crowds of people                                                     
Plictisiți pe drum                                                           Bored on the road                                                          
Și pare un dans ascuns                                                       And it seems like a hidden dance                                           
Supuși, dansează doi necunoscuți                                             Submissive, two strangers dance                                            
[Pre-refren]                                                                 [Pre-Chorus]                                                               
Ochii mei, rușinați, coboară doritor                                         My eyes, ashamed, descend willingly                                        
Dar te respir, în acest urban decor                                          But I breathe you, in this urban setting                                   
You might also like[Refren]                                                  You might also like[Chorus]                                                
Mă ucide ea, mă ucide ea                                                     She's killing me, she's killing me                                         
Încet...                                                                     Slow...                                                                    
Îmi vrea inima, îmi vrea inima                                               He wants my heart, he wants my heart                                       
Din piept                                                                    From the chest                                                             
Mă ucide ea, mă ucide ea                                                     She's killing me, she's killing me                                         
Încet...                                                                     Slow...                                                                    
Îmi vrea inima, îmi vrea inima                                               He wants my heart, he wants my heart                                       
Din piept                                                                    From the chest                                                             
[Punte]                                                                      [Tips]                                                                     
Arde pe asfalt și pulsează foc                                               It burns on the asphalt and pulsates fire                                  
Arde, arde revoltat                                                          It burns, it burns in revolt                                               
Arde prea frumos, arde inima                                                 It burns too beautifully, it burns the heart                               
Arde, recunosc!                                                              It's burning, I admit!                                                     
[Strofa 3]                                                                   [Verse 3]                                                                  
Mă ucide ea încet, încet                                                     She's killing me slowly, slowly                                            
Îmi rupe inima, da, din piept                                                It breaks my heart, yes, out of my chest                                   
Tremură ușor buzele mușcate                                                  Bitten lips tremble slightly                                               
Iar gravitația mă atacă                                                      And gravity attacks me                                                     
Fluturi și vibrații calde pe asfalt                                          Butterflies and warm vibrations on asphalt                                 
De parcă ne plimbăm desculți, prin pat                                       As if we were walking barefoot, in bed                                     
Sirene de incendiu care nu ne pot opri                                       Fire sirens that can't stop us                                             
Iar timpul, un nemernic, numără grăbit                                       And time, an, counts in a hurry                                            
[Outro]                                                                      [Other]                                                                    
Mă ucide ea                                                                  She's killing me                                                           
Mă ucide ea                                                                  She's killing me                                                           
Mă ucide ea                                                                  She's killing me                                                           
Mă ucide ea                                                                  She's killing me                                                           
Da, da...Embed                                                               Yes, yes... Embed                                                          
```

</details>


### Unit Tests

Run unit tests with [pytest](https://docs.pytest.org/en/stable/) and report coverage.
```
pytest
```
