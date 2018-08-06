import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_api_key='iam_api_key'
)
translation = language_translator.translate(
    text='Hello',
    model_id='en-es')
print(json.dumps(translation, indent=2, ensure_ascii=False))