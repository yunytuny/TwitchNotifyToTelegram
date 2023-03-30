import time
import requests
import json

# Twitch API credentials
client_id = 'jvatpoll09jilst9abwyuv0u95j8wj' # paste your client id
client_secret = 'zo71ij5y6kcbqbf5tlk5dnmwtcf6h8' # paste your client secret

# Telegram API credentials
bot_token = '5880682505:AAECVoh2SKZxqS8oTCqf8YIHOLSlHLJ2uaQ' # your bot token from telegram from @BotFather
chat_id = '-1001813698918' # your channel chat id

# Streamer name
streamer = 'neksjgg' # your or your favorite streamer nickname

# Check if streamer is live
token = "g3h4se6z41egyko1syxfotki0yxsjv" # paste your oAuth token from token.py
url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {token}'
}

while True:
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    if data['data']:
        message = f'{streamer} подрубил! https://www.twitch.tv/{streamer}'
        # Send notification to Telegram channel
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': message}
        requests.post(url, data=data)
        time.sleep(36000)  # only after 10 hour code will again check if streamer live
    else:
        print(f'{streamer} is offline!')
        time.sleep(60)  # after one minute code will again check if streamer live
