# TwitchNotifyToTelegram
That code will notify your subscribers at your telegram channel when you start your stream at Twitch.


**Instructions:**

**First**: *Go to dev.twitch.tv and login to your twitch account*

**Second**: *Go to Console and create Extension*

**Third**: *Go to your extension and copy your Twitch API Client ID. Paste your Twitch API Client ID instead of YOUR_CLIENT_ID in token.py and twitch.py.*

**Four**: *Go to Extension settings and generate Twitch API Client Secret. Paste your Twitch API Client Secret instead of YOUR_CLIENT_SECRET in token.py and twitch.py.*

**Five**: *Generate your oAuth token in token.py and paste your oAuth token instead of YOUR_OAUTH_TOKEN in twitch.py.*

**Six**: *Change STREAMER_NAME to your nickname on twitch or your favorite streamer nickname.*

**Seven**: *Change YOUR_BOT_TOKEN to your bot token that you took from @BotFather*

**Final**: *Change YOUR_CHAT_ID to chat id of your telegram channel, you can get it from Get My ID bot by forward the message from your channel**


Note: 
•If nothing appears when you generating the token, so you specified something wrong.
Double check client id and client secret which you entered.

•If you have configured the script, but when you try to send an alert, it is written to you that the streamer is offline, you may not have specified something.
Basically this is an error in the OAuth token, to check this you can write "print(data)" before "while True:"
If first string is {'error': 'Unauthorized', 'status': 401, 'message': 'Invalid OAuth token'} it means you have specified an incorrect OAuth token.

•If you find bug, write to me in a telegram. (@Juipy)
