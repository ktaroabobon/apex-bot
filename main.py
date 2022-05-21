import os
import requests


def main() -> None:
    api_key = os.environ["APEX_API_KEY"]
    print(f"API KEY: {api_key}")

    mode = "store"
    url = f"https://api.mozambiquehe.re/{mode}"
    params = {
        "auth": "d6a85a76dc54e94e886613240df5d2de",
        # "uid": "1014171384068",
        # "platform": "PC",
        # "history": 1,
        # "action": "info",
        # "version": 2,
    }

    res = requests.get(url, params=params)

    print(res.text)


if __name__ == '__main__':
    main()
