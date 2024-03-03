import time
import requests
import json
import telebot
import os
import sys
from telebot import types

if os.path.isfile(os.path.join('settings.json')): # Checking if settings file existing
    with open('settings.json') as file:
        settings = json.load(file)
else:
    print('Settings file doesn`t exist, creating...')
    with open('settings.json', 'w', encoding="utf-8") as f:
        file = {
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "API_TOKEN": "YOUR_BOT_TOKEN",
  "channel_id": "YOUR_CHANNEL_ID",
  "streamer": "STREAMER_NAME",
  "token": "YOUR_OAUTH_TOKEN"
}
        json.dump(file, f, indent=4)
        sys.exit()

if settings['token'] == 'YOUR_OAUTH_TOKEN':
    print('Generating new OAuth token')
    os.system('oauth_token.py')
else:
    pass
    

# Twitch API credentials
client_id = settings['client_id']
client_secret = settings['client_secret']
token = settings['token']

# Telegram API credentials
API_TOKEN = settings['API_TOKEN']
channel_id = settings['channel_id']

# Streamer name
streamer = settings['streamer']

url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {token}'
}

# Check if streamer is live
while True:
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    bot = telebot.TeleBot(API_TOKEN)
    @bot.message_handler()
    
    def notification(): # function who sends notify in telegram channel;
        markup_inline = types.InlineKeyboardMarkup()
        watch_stream = types.InlineKeyboardButton(text = "Watch stream", url = f'https://twitch.tv/{streamer}')
        markup_inline.add(watch_stream)
        bot.send_message(chat_id = channel_id, text = f'{streamer} is now live!\n<b>Title:</b> <code>{title}</code>\n<b>Category:</b> <code>{category}</code>\nhttps://twitch.tv/{streamer}', disable_web_page_preview = True, reply_markup = markup_inline, parse_mode='HTML')
    
    if 'message' in data:
        if data['message'] == 'Invalid OAuth token':
            os.system('oauth_token.py')
            python = sys.executable
            os.execl(python, python, *sys.argv)
    else:
        pass
    if data['data']:
        # Send notification to Telegram channel
        print("Sending notify to your channel and go to sleep at 10 hours")
        title = data['data'][0]['title'] # Getting title of stream
        category = data['data'][0]['game_name'] # Getting category of stream
        notification()
        time.sleep(36000)  # only after 10 hour code will again check if streamer live
    else:
        print(f'{streamer} is offline! Another check after one minute.')
        time.sleep(60)  # after one minute code will again check if streamer live
