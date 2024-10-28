from lyricsgenius import Genius
import re
from bs4 import BeautifulSoup


class PatchedGenius(Genius):  # pragma: no cover
    """
    A patched version of Genius with @xanthon's fixes to remove ads and unwanted content in lyrics
    Credit: @xanthon from https://github.com/johnwmillr/LyricsGenius/pull/272 . Thanks!
    """

    def __init__(self, *args, **kwargs):
        super(PatchedGenius, self).__init__(*args, **kwargs)

    def lyrics(self, song_id=None, song_url=None, remove_section_headers=False):
        """Uses BeautifulSoup to scrape song info off of a Genius song URL
        You must supply either `song_id` or song_url`.
        Args:
            song_id (:obj:`int`, optional): Song ID.
            song_url (:obj:`str`, optional): Song URL.
            remove_section_headers (:obj:`bool`, optional):
                If `True`, removes [Chorus], [Bridge], etc. headers from lyrics.
        Returns:
            :obj:`str` \\|‌ :obj:`None`:
                :obj:`str` If it can find the lyrics, otherwise `None`
        Note:
            If you pass a song ID, the method will have to make an extra request
            to obtain the song's URL and scrape the lyrics off of it. So it's best
            to pass the method the song's URL if it's available.
            If you want to get a song's lyrics by searching for it,
            use :meth:`Genius.search_song` instead.
        Note:
            This method removes the song headers based on the value of the
            :attr:`Genius.remove_section_headers` attribute.
        """
        msg = "You must supply either `song_id` or `song_url`."
        assert any([song_id, song_url]), msg
        if song_url:
            path = song_url.replace("https://genius.com/", "")
        else:
            path = self.song(song_id)["song"]["path"][1:]
        # Scrape the song lyrics from the HTML
        html = BeautifulSoup(
            self._make_request(path, web=True).replace("<br/>", "\n"), "html.parser"
        )
        # Determine the class of the div
        divs = html.find_all("div", class_=re.compile("^lyrics$|Lyrics__Container"))
        if divs is None or len(divs) <= 0:
            if self.verbose:
                print(
                    "Couldn't find the lyrics section. "
                    "Please report this if the song has lyrics.\n"
                    "Song URL: https://genius.com/{}".format(path)
                )
            return None

        # remove ads from div
        ads = html.find("div", {"class": re.compile("RightSidebar__Container")})
        ads.decompose()
        # remove header
        header = html.find("div", {"class": re.compile("LyricsHeader__Container")})
        header.decompose()
        # remove embed note / footer
        footer = html.find("div", {"class": re.compile("LyricsFooter__Container")})
        footer.decompose()

        lyrics = "\n".join([div.get_text() for div in divs])

        # Remove [Verse], [Bridge], etc.
        if self.remove_section_headers or remove_section_headers:
            lyrics = re.sub(r"(\[.*?\])*", "", lyrics)
            lyrics = re.sub("\n{2}", "\n", lyrics)  # Gaps between verses
        return lyrics.strip("\n")
