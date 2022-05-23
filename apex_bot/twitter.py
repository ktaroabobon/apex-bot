import os

import tweepy

TWITTER_API_KEY = os.environ["TWITTER_API_KEY"]
TWITTER_API_KEY_SECRET = os.environ["TWITTER_API_KEY_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
TWITTER_ACCOUNT_ID = os.environ["TWITTER_ACCOUNT_ID"]


def tweet(tweet_content: str):
    """Twitter APIを用いてツイートを行う

    Args:
        tweet_content(str): ツイート内容
    """
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    )

    client = tweepy.API(auth)
    media_url = "https://apexlegendsstatus.com/assets/maps/Worlds_Edge.png"
    client.update_status_with_media(status=tweet_content, filename=media_url)


if __name__ == '__main__':
    content = "こんにちは"
    tweet(content)
