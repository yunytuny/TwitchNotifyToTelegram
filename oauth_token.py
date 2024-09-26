import requests
import json

with open('settings.json') as set:
    settings = json.load(set)

client_id = settings['client_id'] 
client_secret = settings['client_secret'] 

# Request an OAuth token
url = 'https://id.twitch.tv/oauth2/token'
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}
response = requests.post(url, data=data)

# If you write wrong client_secret
if response.status_code == 403:
    print(f'Wrong client_secret')

# If you write wrong client_id
elif response.status_code == 400:
    print(f'Wrong client_id')

# Extract the OAuth token from the response
if response.status_code == 200:
    data = response.json()
    settings['token'] = data['access_token']
    print('Generated new token')
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)
