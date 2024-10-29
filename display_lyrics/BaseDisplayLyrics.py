from abc import ABC, abstractmethod


class BaseDisplayLyrics(ABC):

    @abstractmethod
    def display_lyrics(self, **kwargs):
        """
        Display original and English translated lyrics
        """
