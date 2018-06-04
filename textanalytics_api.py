# Author: Parashar Shah
# Chapter: Cognitive Services
# Version: 1.0
# Date: May 25, 2018
# Replace <Subscription Key> with your valid subscription's api access key.
subscription_key = "<Access Key>"
assert subscription_key

# Replace the base url with what you see as Endpoint in the portal’s Overview section under your api

text_analytics_base_url = "https://westus2.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentiment_api_url = text_analytics_base_url + "sentiment"

# Send the text you want the api to analyze
# You can send multiple texts
documents = {'documents' : [
  {'id': '1', 'text': 'I am excited about using AI offerings by Microsoft.'},
]}

import requests

# Get sentiment of text
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
print(sentiments)

# Get the language of text
language_api_url = text_analytics_base_url + "languages"
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
print(languages)

# Get key phrases from text
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
print(key_phrases)

# Get well-known entities
entity_linking_api_url = text_analytics_base_url + "entities"
response  = requests.post(entity_linking_api_url, headers=headers, json=documents)
entities = response.json()
print(entities)
