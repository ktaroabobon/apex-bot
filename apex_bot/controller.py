import datetime

from dateutil import tz

from als import get_info
from twitter import tweet

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
}

TZ_INFO = "Asia/Tokyo"


def get_tweet_content(map_info: dict, mode: str = "battle_royale"):
    """マップ情報からツイート内容を取得

    Args:
        map_info(dict): マップ情報
        mode(str): マップモード

    Returns:
        str: ツイート内容
    """
    target_data = map_info[mode]
    start = target_data['current']['start']
    end = target_data['current']['end']
    jst = tz.gettz(TZ_INFO)

    info = {
        'start': datetime.datetime.fromtimestamp(start).astimezone(jst),
        'end': datetime.datetime.fromtimestamp(end).astimezone(jst),
        'map': MAP_NAME_DICT[(target_data['current']['map']).lower()],
        'asset': target_data['current']['asset'],
        'next_map': MAP_NAME_DICT[(target_data['next']['map']).lower()],
    }

    context = f"""
    【モード】
{MODE_DICT[mode]}
    
【現在のマップ】
{info['map']}（{str(info['start'].hour).zfill(2)}:{str(info['start'].minute).zfill(2)}～{str(info['end'].hour).zfill(2)}:{str(info['end'].minute).zfill(2)}）
    
【次回のマップ】
{info['next_map']}（{str(info['start'].hour).zfill(2)}:{str(info['start'].minute).zfill(2)}～{str(info['end'].hour).zfill(2)}:{str(info['end'].minute).zfill(2)}）   
    """

    return context


def bot():
    map_info = get_info()
    content = get_tweet_content(map_info)
    tweet(content)


if __name__ == '__main__':
    bot()
