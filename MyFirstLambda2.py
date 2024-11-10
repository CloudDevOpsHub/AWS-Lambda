import json

def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("Received event: " + json.dumps(event, indent=2))

    # Check if it's a POST request and has a body
    if event['httpMethod'] == 'POST' and event['body']:
        body = json.loads(event['body'])
        message = body.get('message', 'No message provided')
        return {
            'statusCode': 200,
            'body': json.dumps(f"Your message was: {message}")
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Please send a POST request with a valid message')
        }
