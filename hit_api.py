# sample file to hit the API

import requests
import json


def hit_api():
    url = 'http://localhost:5000/limit'
    responses = []
    for i in range(10):
        response = requests.get(url)
        responses.append(response.json())
    return responses

if __name__ == '__main__':
    responses = hit_api()
    print(json.dumps(responses, indent=4))