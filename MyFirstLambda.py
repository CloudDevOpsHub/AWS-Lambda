import json

def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("Received event: " + json.dumps(event, indent=2))

    # Return a simple response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from AWS Lambda!')
    }
