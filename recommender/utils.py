import requests
from django.conf import settings

def GetFoodRec(query):
    endpoint = 'https://api.openai.com/v1/completions'
    headers = {
        'Authorization': f'Bearer {settings.OPENAI_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': query,
        'max_tokens': 100,
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None
