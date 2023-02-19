"""
Title : 【Python × スクレイピング入門②】
Theme : Requestsを使ってWebページにアクセスしてみよう！
URL   : https://www.youtube.com/watch?v=Ly_vLLRPFhw&list=PL4Y-mUWLK2t1LehwHVwAqxXTXw5xd-Yq8&index=2
"""

import requests


# URLにアクセス
url = 'https://www.python.org/'
r = requests.get(url)

# アクセスしたURLの確認
r.url
print(r.url)

# ステータスコード
# --- 200：アクセス成功
# --- 400-499：アクセス失敗（クライアント側のエラー）
# --- 500-599：アクセス失敗（サーバー側のエラー）
r.status_code

# ステータスコードを用いた条件分岐
if r.status_code == 200:
    print("接続成功")
else:
    raise ValueError("error!")

# リクエスト結果の取得
print(r.text)
