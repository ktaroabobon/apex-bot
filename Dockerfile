FROM python:3.8
# 基本的には標準のpythonから作成する

ENV APP_PATH=/code \
    PYTHONPATH=.
#　開発物のソースコードはcodeデイレクトリ下に配置する

WORKDIR $APP_PATH

# コンテナのセットアップ
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install poetry

COPY . .

RUN poetry install
#　必要なパッケージ等をインストールする

EXPOSE 8080