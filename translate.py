import boto3
#Prompts you to enter a two letter code in the console for the language you want to translate to
newLanguage = input('Enter language: ') 
client = boto3.client('translate')
response = client.translate_text(
    #Prompts you to enter text in the console that you want to translate
    Text = input('Enter text: '),
    SourceLanguageCode = 'en',
    TargetLanguageCode = newLanguage,
    )
print(response)
#Translates from target language back to English
reverse = client.translate_text(
    Text = response['TranslatedText'],
    SourceLanguageCode = response['TargetLanguageCode'],
    TargetLanguageCode = response['SourceLanguageCode']
    )
print(reverse)
