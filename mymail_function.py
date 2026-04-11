import json

def lambda_handler(event, context):
    print(event['headers']['X-Forwarded-For'])
    return {
        "statusCode": 200 ,
        "body": "i am mail app, i know your IP :"  + event['headers']['X-Forwarded-For']
    }
