import boto3
client = boto3.client('comprehend')
input = input('Enter text: ')
response = []
response.append(client.detect_sentiment(
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_entities(
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_key_phrases(
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_syntax(
    Text = input,
    LanguageCode='en'
    ))
for i in response:
    print(i)
