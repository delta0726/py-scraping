"""
Theme : BeautifulSoupを使ったスクレイピング
Page  : ファイルのみ
"""

from bs4 import BeautifulSoup
import requests


# URLの指定
url = "https://www.amazon.co.jp/gp/bestsellers/books/466298"

# URLにアクセス
response = requests.get(url)
print(response)

# HTMLの構文解析
soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup))

# p13n-asin-index-0 > div.zg-grid-general-faceout > div > a:nth-child(2) > span > div

# $$('css selector')
# $x('xpath')

# $$('.zg-grid-general-faceout')

# $$('.zg-grid-general-faceout')[0].textContent
# '統計学の基礎から学ぶExcelデータ分析の全知識（できるビジネス） できるビジネスシリーズ三好大悟5つ星のうち4.2 185Kindle版￥1,881900ポイント(48%)'


items = soup.select('.zg-grid-general-faceout')

for item in items:
    print(item.text)
