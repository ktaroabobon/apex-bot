import os

import tweepy

TWITTER_API_KEY = os.environ["TWITTER_API_KEY"]
TWITTER_API_KEY_SECRET = os.environ["TWITTER_API_KEY_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
TWITTER_ACCOUNT_ID = os.environ["TWITTER_ACCOUNT_ID"]


def tweet(tweet_content: str, media_path: str = None):
    """Twitter APIを用いてツイートを行う

    Args:
        tweet_content(str): ツイート内容
        media_path(str): 画像のパス
    """
    print(media_path)
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    )

    client = tweepy.API(auth)
    if media_path is not None:
        client.update_status_with_media(status=tweet_content, filename=media_path)
    else:
        client.update_status(status=tweet_content)
