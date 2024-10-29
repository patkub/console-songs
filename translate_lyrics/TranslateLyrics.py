import requests, uuid
from requests.exceptions import RequestException


class TranslateLyrics:
    def __init__(self, translator_key, region):
        """
        Translate song lyrics using Microsoft Azure AI Translator
        @param translator_key: string access token for Azure Translator Resource https://learn.microsoft.com/en-us/azure/ai-services/translator/create-translator-resource
        @param region: string region for Azure Translator Resource
        """
        self.subscription_key = translator_key
        self.region = region

    def translate_lyrics(self, lyrics):
        """
        Translates lyrics to English using Microsoft Azure AI Translator

        @param lyrics: string song lyrics in foreign language
        @return: string song lyrics in english
        """
        # If you encounter any issues with the base_url or path, make sure
        # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
        endpoint = "https://api.cognitive.microsofttranslator.com/"
        path = "/translate?api-version=3.0"
        # from romanian to english
        # params = '&from=ro&to=en'
        # or detect original language, and translate to english
        params = "&to=en"
        constructed_url = endpoint + path + params

        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }

        # You can pass more than one object in body.
        body = [{"text": lyrics}]

        english_translation = ""
        try:
            request = requests.post(constructed_url, headers=headers, json=body)
            response = request.json()
            english_translation = response[0]["translations"][0]["text"]
        except (RequestException, KeyError):
            # ignore network error, or invalid data
            pass

        return english_translation
