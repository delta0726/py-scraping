"""
Theme : Googleで検索を行って検索結果のリンクを開く
Page  : ファイルのみ
"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# ドライバ接続
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# ブラウザ起動
# --- Googleの検索TOP画面を開く。
driver.get('https://google.com')
driver.get("https://www.google.co.jp/")

# 検索語として「selenium」と入力し、Enterキーを押す。
search = driver.find_element(By.NAME, 'q')
search.send_keys("selenium automation")
search.send_keys(Keys.ENTER)

# 検索結果をクリック
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium WebDriver")
element.click()

# 5秒間待機してみる。
sleep(5)

# ブラウザを終了する。
driver.close()
