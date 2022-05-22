import os
import requests


def main() -> None:
    api_key = os.environ["APEX_API_KEY"]
    print(f"API KEY: {api_key}")

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


if __name__ == '__main__':
    main()
