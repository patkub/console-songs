from abc import ABC, abstractmethod


class BaseDisplayLyrics(ABC):  # pragma: no cover

    @abstractmethod
    def display_lyrics(self, **kwargs):
        """
        Display original and English translated lyrics
        """
        pass
