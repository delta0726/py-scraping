"""
Title : 【Python × スクレイピング入門②】
Theme : 10分で理解！BeautifulSoupで複数の要素を取得する方法(find_all)をマスターしよう！
URL   : https://www.youtube.com/watch?v=8ZmQo8WiAis&list=PL4Y-mUWLK2t1LehwHVwAqxXTXw5xd-Yq8&index=4
"""

import requests
from bs4 import BeautifulSoup


# URLにアクセス
url = 'https://www.python.org/'
r = requests.get(url)

# HTML解析
soup = BeautifulSoup(r.text, "lxml")

# 全てのh2タグの取得
soup.find_all('h2')

# 最初の要素を確認
soup.find_all('h2')[0]
soup.find('h2') == soup.find_all('h2')[0]

# テキストのループ表示
# h2_tag = soup.find_all('h2')[0]
for i, h2_tag in enumerate(soup.find_all('h2')):
    print(i, h2_tag.text)

# テキストの格納
h2_tag_list = []
for i, h2_tag in enumerate(soup.find_all('h2')):
    h2_tag_list.append(h2_tag.text)

# テキスト表示
h2_tag_list
