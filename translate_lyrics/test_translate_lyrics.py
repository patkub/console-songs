from .TranslateLyrics import TranslateLyrics
import requests
from unittest import mock


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_requests_post(*args, **kwargs):
    """
    Mock patch request.post() calls
    @param args:
    @param kwargs:
    @return:
    """

    # TODO: improve this url detection
    if args[0].startswith("https://api.cognitive.microsofttranslator.com/"):
        return MockResponse(
            [{"translations": [{"text": "mocked translated lyrics"}]}], 200
        )

    return MockResponse(None, 404)


def mock_requests_post_invalid(*args, **kwargs):
    """
    Mock patch request.post() calls
    @param args:
    @param kwargs:
    @return:
    """
    return MockResponse([{"fake_bad_data": "bad"}], 200)


def test_translate_lyrics_sets_translator_key():
    """
    Sets translator key
    """
    translator_key = "fake_translator_key"
    region = "eastus"
    translate_lyrics = TranslateLyrics(translator_key, region)
    assert translate_lyrics.subscription_key == translator_key


@mock.patch("requests.post", side_effect=mock_requests_post)
def test_translate_lyrics(mock_req):
    """
    Translates lyrics
    """

    # Prepare: instantiate TranslateLyrics with fake translator key
    translator_key = "fake_translator_key"
    region = "eastus"
    translate_lyrics_obj = TranslateLyrics(translator_key, region)

    # mock_requests_post returns a mocked response from "https://api.cognitive.microsofttranslator.com/"
    # call translate_lyrics_obj.translate_lyrics(lyrics)
    english_translation = translate_lyrics_obj.translate_lyrics("some lyrics")

    # assert it replies with the mocked translated lyrics
    assert english_translation == "mocked translated lyrics"


@mock.patch("requests.post", side_effect=mock_requests_post_invalid)
def test_translate_lyrics_invalid(mock_req):
    """
    Translates lyrics
    """

    # Prepare: instantiate TranslateLyrics with fake translator key
    translator_key = "fake_translator_key"
    region = "eastus"
    translate_lyrics_obj = TranslateLyrics(translator_key, region)

    # mock_requests_post returns a mocked response from "https://api.cognitive.microsofttranslator.com/"
    # call translate_lyrics_obj.translate_lyrics(lyrics)
    english_translation = translate_lyrics_obj.translate_lyrics("some lyrics")

    # assert it replies with the mocked translated lyrics
    assert english_translation == ""


@mock.patch("requests.post", side_effect=mock_requests_post)
def test_mock_requests_post_404(mock_req):
    """
    Test 404
    """

    resp = requests.post("https://example.com/404")
    assert resp.status_code == 404


@mock.patch("requests.post", side_effect=mock_requests_post_invalid)
def test_mock_requests_post_invalid(mock_req):
    """
    Test 404
    """

    resp = requests.post("https://example.com/404")
    resp_json = resp.json()
    assert resp_json[0]["fake_bad_data"] == "bad"
    assert resp.status_code == 200
