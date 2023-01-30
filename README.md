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

If live broadcat at check return true, code send a notify to your telegram channel and go sleep to 10 hours.
If live broadcat at check return fasle, code dont notify and re-check after one minute.

**You can change delay in time.sleep(36000) and time.sleep(60).**
