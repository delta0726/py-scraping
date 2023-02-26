"""
Title : スクレイピング＆クローリングデータ収集
Theme : 秀和システムのデータを取得する（縮小版）
Topic : IT勉強会の情報を取得する（APIの活用）
Page  : P65 - 70
"""

import pandas as pd
import requests
import json


def get_event(keyword, ym, output):
    # リクエストの作成
    base_url = "https://connpass.com/api/v1/event/?"
    keyowrd_query = f"keyword={keyword}"
    ym_query = f"ym={ym}"
    query = base_url + "&" .join([keyowrd_query, ym_query])

    # APIの実行
    response = requests.get(query)

    # データ取得
    event_json = json.loads(response.text)["events"]

    df = pd.DataFrame(event_json)
    df = df.loc[:, ['title', 'catch', 'started_at', 'event_url']]

    return df.to_csv(output, index=False)


if __name__ == "__main__":

    # パラメータ設定
    KEYWORLD = "Python"
    YM = 202303
    OUTPUT = "sec4_hobby/output/02_compass.csv"

    # データ取得
    get_event(keyword=KEYWORLD, ym=YM, output=OUTPUT)
