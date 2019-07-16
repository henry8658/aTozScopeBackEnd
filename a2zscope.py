import boto3
import base64
import json
import validators

AWS_SERVICE = 'rekognition'
AWS_REGION_NAME = 'us-west-2'
AWS_FEATURE_TYPE = 'TextDetections'

def lambda_handler(event, context):
    client=boto3.client(AWS_SERVICE, AWS_REGION_NAME)

    encodedPhoto = event['photo'] 
    decodedPhoto = {'Bytes': base64.b64decode(encodedPhoto)}

    response=client.detect_text(Image=decodedPhoto)
    textDetections=response[AWS_FEATURE_TYPE]

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
