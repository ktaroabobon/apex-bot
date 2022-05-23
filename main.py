import json
import os
import pathlib
import requests


def main() -> None:
    api_key = os.environ["ALS_API_KEY"]
    print(f"ALS API KEY: {api_key}")

    mode = "maprotation"
    url = f"https://api.mozambiquehe.re/{mode}"
    params = {
        "auth": api_key,
        # "uid": "1014171384068",
        # "platform": "PC",
        # "history": 1,
        # "action": "info",
        "version": 2,
    }

    res = requests.get(url, params=params)

    print(res.text)

    path = pathlib.Path().resolve() / f"data.json"

    with path.open('w') as f:
        json.dump(json.loads(res.text), f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
