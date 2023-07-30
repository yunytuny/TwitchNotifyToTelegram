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
channel_id = 'YOUR_CHANNEL_ID' # your channel chat id

# Streamer name
streamer = 'STREAMER_NAME' # your or your favorite streamer nickname

#Twitch token from token.py
token = "YOUR_OAUTH_TOKEN" # paste your oAuth token from token.py

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
        watch_stream = types.InlineKeyboardButton(text = "Смотреть стрим", url = f'https://twitch.tv/{streamer}')
        markup_inline.add(watch_stream)
        bot.send_message(chat_id = channel_id, text = f'{streamer} запустил стрим!\n<b>Название:</b> <code>{title}</code>\n<b>Категория:</b> <code>{category}</code>\nhttps://twitch.tv/{streamer}', disable_web_page_preview = True, reply_markup = markup_inline, parse_mode='HTML')
    
    if data['message'] == 'Invalid OAuth token':
        print("You have a invalid oauth token!\nGenerate new in token.py")
        break
    
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
