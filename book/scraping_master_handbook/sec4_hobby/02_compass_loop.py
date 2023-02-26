"""
Title   : スクレイピング＆クローリングデータ収集
Section : 4 趣味に活かす情報収集偏
Theme   : IT勉強会の情報を取得する（APIの活用・ループ版）
Date    : 2023/2/26
Page    : P65 - 70
"""

import pandas as pd
import requests
import json


def get_event(keyword, ym):
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

    return df


if __name__ == "__main__":

    # パラメータ設定
    start_date = '2023-03-01'
    end_date = '2023-03-31'
    request_month = pd.date_range(start_date, end_date, freq='MS').strftime("%Y%m").tolist()

    # 格納用リスト
    df_list = []

    # request_ym = request_month[0]
    for request_ym in request_month:

        # パラメータ設定
        KEYWORLD = "Python"
        YM = request_ym
        OUTPUT = "sec4_hobby/output/02_compass.csv"

        # データ取得
        df = get_event(keyword=KEYWORLD, ym=YM)
        df_list.append(df)

    # ファイル保存
    df_agg = pd.concat(df_list)
    df_agg.to_csv("sec4_hobby/output/02_compass_loop.csv", index=False)
