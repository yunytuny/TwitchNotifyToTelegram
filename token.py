import requests

client_id = 'YOUR_CLIENT_ID' # paste your client id
client_secret = 'YOUR_CLIENT_SECRET' # paste your client secret

# Request an OAuth token
url = 'https://id.twitch.tv/oauth2/token'
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}
response = requests.post(url, data=data)

# Extract the OAuth token from the response
if response.status_code == 200:
    data = response.json()
    token = data['access_token']
    print("Your oAuth token is: " + token)
