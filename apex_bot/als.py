import json
import os
import requests

ALS_API_KEY = os.environ["ALS_API_KEY"]


def get_info(version=2):
    """ALS-APIを用いて情報を取得する

    Returns:
        dict: 取得した情報

    Notes:
        一旦マップローテーションのみ
    """
    mode = "maprotation"
    url = f"https://api.mozambiquehe.re/{mode}"
    params = {
        "auth": ALS_API_KEY,
        "version": version
    }

    res = requests.get(url, params=params)

    return json.loads(res.text)


if __name__ == '__main__':
    data = get_info()
    print(data)
    print(f"type: {type(data)}")
