import json
import requests

def lambda_handler(event, context):
    subnet_id = event.get("subnet_id", "subnet-unknown")
    name = "Anurag Dangi"
    email = "anurag.suraj23@gmail.com"

    url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    headers = {"X-Siemens-Auth": "test"}
    payload = {
        "subnet_id": subnet_id,
        "name": name,
        "email": email
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()

    return {
        "statusCode": response.status_code,
        "body": json.dumps(response_data)
    }

