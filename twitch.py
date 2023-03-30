import time
import requests
import json

# Twitch API credentials
client_id = 'YOUR_CLIENT_ID' # paste your client id
client_secret = 'YOUR_CLIENT_SECRET' # paste your client secret

# Telegram API credentials
bot_token = 'YOUR_BOT_TOKEN' # your bot token from telegram from @BotFather
chat_id = 'TOKEN_ID_YOUR_CHANNEL' # your channel chat id

# Streamer name
streamer = 'STREAMER_NAME' # your or your favorite streamer nickname

# Check if streamer is live
token = "YOUR_OAUTH_TOKEN" # paste your oAuth token from token.py
url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {token}'
}

while True:
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    if data['data']:
        message = f'{streamer} go live! https://www.twitch.tv/{streamer}'
        # Send notification to Telegram channel
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': message}
        requests.post(url, data=data)
        time.sleep(36000)  # only after 10 hour code will again check if streamer live
    else:
        print(f'{streamer} is offline!')
        time.sleep(60)  # after one minute code will again check if streamer live
