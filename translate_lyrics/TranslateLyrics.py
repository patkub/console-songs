import requests, uuid


class TranslateLyrics:
    def __init__(self, translator_key):
        """
        Translate song lyrics using Microsoft Azure AI Translator
        @param translator_key: string access token for Azure Translator Resource https://learn.microsoft.com/en-us/azure/ai-services/translator/create-translator-resource
        """
        self.subscription_key = translator_key

    def translate_lyrics(self, lyrics):
        """
        Fetches lyrics for a song given its name and artist

        @param lyrics: string song lyrics in foreign language
        @return: string song lyrics in english
        """
        # If you encounter any issues with the base_url or path, make sure
        # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
        endpoint = "https://api.cognitive.microsofttranslator.com/"
        path = '/translate?api-version=3.0'
        # from romanian to english
        # params = '&from=ro&to=en'
        # or detect original language, and translate to english
        params = '&to=en'
        constructed_url = endpoint + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Ocp-Apim-Subscription-Region': 'eastus',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': lyrics
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        english_translation = response[0]["translations"][0]["text"]

        return english_translation
