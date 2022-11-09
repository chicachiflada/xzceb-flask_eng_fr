"""
Creating translator functions
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator=IAMAuthenticator('232551oT2a_QD0K0DzBxT610mMn5IJgnSHxk10l1WsOv')
language_translator= LanguageTranslatorV3(
    version='2018_05_01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/215b4d16-1169-46a0-b3e7-5f0932f6f0cc')

# translating to French
def english_to_french(english_text):
    #write the code here
    """
    This function translates text from English to French and returns the French text
    """
    translation = language_translator.translate(
        text=english_text,
        model_id="en-fr").get_result()
    french_text=translation['translation'][0]['translation']
    return french_text

 #translating to English
def french_to_english(french_text):
    #write the code here
    """
    This function translates text from French to English and returns the English text
    """
    english_translation=language_translator.translate(
        text=french_text,
        model_id="fr-en").get_result()
    english_text=english_translation['translation'][0]['translation']
    return english_text
