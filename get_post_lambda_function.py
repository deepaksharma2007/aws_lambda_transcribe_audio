import json

def lambda_handler(event, context):
    if event['httpMethod' ] == "GET":
        print(event['queryStringParameters']['name' ])
        print("i m GET method")

    elif event['httpMethod'] == "POST":
        print("i m POST")
        print(event)

    else:
        print("idk this method")

    return {
        'statusCode': 200,
        'body': "Welcome To the world of success:-  " + event['queryStringParameters']['name']
    }

# It is useful to use queryStringParameters variable in code when we pass variables; otherwise, it fails
# https://h00qlebzf0.execute-api.ap-south-1.amazonaws.com/test/devops?name=deepak&country=India
