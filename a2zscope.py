import boto3
import base64
import json

def lambda_handler(event, context):
    detected_text = []
    photo = event['photo'] 
    client=boto3.client('rekognition', region_name='us-west-2')
    response=client.detect_text(Image={'Bytes': base64.b64decode(photo)})
    texDetections=response['TextDetections']
    for text in textDetections:
        detected_text.append(text['DetectedText'])

    urls = set()
    for url in detected_text:
        url.split(' ')
        if validators.url(url) == True:
            urls.add(url)
return { 
    urls : list(urls)
}
