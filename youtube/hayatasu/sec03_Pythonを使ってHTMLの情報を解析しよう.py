"""
Title : 【Python × スクレイピング入門②】
Theme : BeautifulSoupとは？Pythonを使ってHTMLの情報を解析しよう！【演習あり】
URL   : https://www.youtube.com/watch?v=6LOF2hiMbN0&list=PL4Y-mUWLK2t1LehwHVwAqxXTXw5xd-Yq8&index=3
"""

import requests
from bs4 import BeautifulSoup


# URLにアクセス
url = 'https://www.python.org/'
r = requests.get(url)

# 確認
r.text
type(r.text)

# HTML解析
soup = BeautifulSoup(r.text, "lxml")

# h2タグの取得
soup.h2
soup.find('h2')


# ＜ポイント＞
# - タグを取得するとき：soup.find()
# - 複数タグを取得するとき：soup.find_all()
# - テキストを取得するとき：soup.find().text

# h2タグのテキスト取得
soup.h2.text
soup.find('h2').text

# get_text()による取得
# --- 著者はつかわない模様（Noneが返るのを避ける）
soup.h2.get_text()
soup.find('h2').get_text()

# getメソッドの振舞い
# --- Noneが返ることによってエラーを避けることができる
# --- 逆にNoneという結果が返ってしまう
d = {'apple': 100}
print(d.get('apple'))
print(d.get('banana'))


# 演習 --------------------------------------------------

# import requests
# from bs4 import BeautifulSoup

# URLにアクセス
url = 'https://tech-diary.net/python-scraping-books'
r = requests.get(url)

# HTML解析
# --- r.textを解析
soup = BeautifulSoup(r.text, "lxml")

# h1タグの取得
soup.h1
soup.find('h1')
