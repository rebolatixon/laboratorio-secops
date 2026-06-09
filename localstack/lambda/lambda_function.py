import json


def lambda_handler(event, context):
    print(f"Evento recebido: {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
