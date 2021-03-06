#https://boto3.readthedocs.io/en/latest/reference/services/comprehend.html

import boto3
client = boto3.client('comprehend')
#Prompts you to input text in the console to be analyzed
input = input('Enter text: ')
#Creates an array and adds each method to the list
response = []
response.append(client.detect_sentiment(    #detects the "Tone" of the inputted text: Positive, Neutral, Mixed or Negative
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_entities(     #detects proper nouns, dates, etc. in the input
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_key_phrases(  #detects key phrases and ideas in the input
    Text = input,
    LanguageCode='en'
    ))
response.append(client.detect_syntax(       #detects the part of speech for each word in the input
    Text = input,
    LanguageCode='en'
    ))
for i in response:
    print(i) 
