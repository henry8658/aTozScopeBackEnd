import boto3
import base64
import json
import validators

def lambda_handler(event, context):
    client=boto3.client('rekognition', region_name='us-west-2')

    encodedPhoto = event['photo'] 
    decodedPhoto = {'Bytes': base64.b64decode(encodedPhoto)}

    response=client.detect_text(Image=decodedPhoto)
    textDetections=response['TextDetections']

    detected_text = []
    for text in textDetections:
        detected_text.append(text['DetectedText'])

    urls = set()
    for url in detected_text:
        url.split()
        if validators.url(url):
            urls.add(url)

    return {
        urls : list(urls)
    }
