import time
import requests
import json
import telebot
from telebot import types

# Twitch API credentials
client_id = 'YOUR_CLIENT_ID' # paste your client id
client_secret = 'YOUR_CLIENT_SECRET' # paste your client secret

# Telegram API credentials
API_TOKEN = 'YOUR_BOT_TOKEN' # your bot token from telegram from @BotFather
channel_id = 'YOUR_CLIENT_ID' # your channel chat id

# Streamer name
streamer = 'STREAMER_NAME' # your or your favorite streamer nickname
streamerm = streamer.replace("_", "")

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
    title = data['data'][0]['title'] # Getting title of stream
    category = data['data'][0]['game_name'] # Getting category of stream

    bot = telebot.TeleBot(API_TOKEN)
    @bot.message_handler()
    def notification(): # function who sends notify in telegram channel;
        markup_inline = types.InlineKeyboardMarkup()
        watch_stream = types.InlineKeyboardButton(text = "Смотреть стрим", url = f'https://twitch.tv/{streamer}')
        markup_inline.add(watch_stream)
        bot.send_message(chat_id = channel_id, text = f'{streamerm} is now live\!\n**Title:** `{title}`\n**Category:** `{category}`\nhttps://twitch\.tv/{streamer}', disable_web_page_preview = True, reply_markup = markup_inline, parse_mode='MarkdownV2')
    if data['data']:
        # Send notification to Telegram channel
        print("Sending notify to your channel")
        notification()
        time.sleep(36000)  # only after 10 hour code will again check if streamer live
    else:
        print(f'{streamer} is offline!')
        time.sleep(60)  # after one minute code will again check if streamer live
