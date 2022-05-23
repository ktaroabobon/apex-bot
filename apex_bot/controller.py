import datetime
from pathlib import Path

from dateutil import tz

from apex_bot.als import get_info
from apex_bot.twitter import tweet

MODE_DICT = {
    "battle_royale": "BR カジュアル",
    "arenas": "アリーナ",
    "ranked": "BR ランク",
    "arenasRanked": "アリーナ　ランク",
    "control": "コントロール"
}

MAP_NAME_DICT = {
    "olympus": "オリンパス",
    "world's edge": "ワールズエッジ",
    "storm point": "ストームポイント",
    "kings canyon": "キングスキャニオン",
    "party crasher": "パーティークラッシャー",
    "overflow": "オーバーフロー",
}

TZ_INFO = "Asia/Tokyo"
MEDIA_DIR = Path().resolve() / "media"


def get_tweet_content(map_info: dict, mode: str = "battle_royale") -> dict:
    """マップ情報からツイート内容を取得

    Args:
        map_info(dict): マップ情報
        mode(str): マップモード

    Returns:
        dict: ツイート内容(内容、画像url)
    """
    target_data = map_info[mode]
    start = target_data['current']['start']
    end = target_data['current']['end']
    next_start = target_data['next']['start']
    next_end = target_data['next']['end']
    jst = tz.gettz(TZ_INFO)

    info = {
        'start': datetime.datetime.fromtimestamp(start).astimezone(jst),
        'end': datetime.datetime.fromtimestamp(end).astimezone(jst),
        'next_start': datetime.datetime.fromtimestamp(next_start).astimezone(jst),
        'next_end': datetime.datetime.fromtimestamp(next_end).astimezone(jst),
        'map': MAP_NAME_DICT[(target_data['current']['map']).lower()],
        'asset': MEDIA_DIR / target_data['current']['asset'].split('/')[-1],
        'next_map': MAP_NAME_DICT[(target_data['next']['map']).lower()],
    }

    context = f"""
    【モード】
{MODE_DICT[mode]}
    
【現在のマップ】
{info['map']}（{str(info['start'].hour).zfill(2)}:{str(info['start'].minute).zfill(2)}～{str(info['end'].hour).zfill(2)}:{str(info['end'].minute).zfill(2)}）
    
【次回のマップ】
{info['next_map']}（{str(info['next_start'].hour).zfill(2)}:{str(info['next_start'].minute).zfill(2)}～{str(info['next_end'].hour).zfill(2)}:{str(info['next_end'].minute).zfill(2)}） 
#Apex #Maprotation
    """

    return {'text': context, 'media': info['asset']}


def bot():
    """Twitterのbotを動かす関数
    """
    map_info = get_info()
    content = get_tweet_content(map_info)
    content_text = content['text']
    media_url = content['media']
    if media_url.exists():
        tweet(content_text, str(media_url))
    else:
        tweet(content_text)


if __name__ == '__main__':
    bot()
