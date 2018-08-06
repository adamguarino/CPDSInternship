import boto3
client = boto3.client('translate')
response = client.translate_text(
    Text = input('Enter text: '),
    SourceLanguageCode = 'en',
    TargetLanguageCode = 'it'
    )
print(response)
reverse = client.translate_text(
    Text = response['TranslatedText'],
    SourceLanguageCode = response['TargetLanguageCode'],
    TargetLanguageCode = response['SourceLanguageCode']
    )
print(reverse)