import json
from watson_developer_cloud import LanguageTranslatorV3

#Establishes the version and key used to connect to the translator. Key should be replaced with the key generated for you on IBM's website
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_api_key='iam_api_key'
)

#Allows the user to input text in the console to be translated
inputText = input("Enter text: ")
translation = language_translator.translate(
    text=inputText,
    model_id='en-es')
print(json.dumps(translation, indent=2, ensure_ascii=False))
