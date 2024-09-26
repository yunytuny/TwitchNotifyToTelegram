# TwitchNotifyToTelegram
That code will notify your followers at your telegram channel when you start your stream at Twitch.


**Preview:**

![preview](https://raw.githubusercontent.com/yunytuny/TwitchNotifyToTelegram/main/images/preview.png)




**Instructions:**

**First**: *Go to dev.twitch.tv and login to your twitch account*

**Second**: *Go to Console and create Extension*

**Third**: *Go to your extension and copy your Twitch API Client ID. Paste your Twitch API Client ID instead of YOUR_CLIENT_ID in settings.json*

**Four**: *Go to Extension settings and generate Twitch API Client Secret. Paste your Twitch API Client Secret instead of YOUR_CLIENT_SECRET in settings.json*

**Five**: *OAuth token will be automatically generated by opening twitch.py*

**Six**: *Change STREAMER_NAME to your nickname on twitch or your favorite streamer nickname.*

**Seven**: *Change YOUR_BOT_TOKEN to your bot token that you took from @BotFather*

**Final**: *Change YOUR_CHAT_ID to chat id of your telegram channel, you can get it from Get My ID bot by forward the message from your channel**

**Optional**: In *twitch.py* there are a couple of settings:

    (False by default)
    stream_over - If you want to send a post about the end of the stream, set True 
    delete_post - If you want to delete notification post after the end of the stream, set True

///

•If you find bug or you have troubles with code, write to me in a telegram channel. (@yunytunygithub)
