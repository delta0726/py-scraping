"""
Theme : 秀和システムのデータを取得する（縮小版）
Page  : 29 - 32
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    try:
        # ブラウザのドライバーの取得
        # Selenium4 WebDriver の executable_path 使用に伴う警告の回避方法
        # --- https://gammasoft.jp/blog/python-selenium-webdriver-deprecation-warning-by-executable_path/
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Webページにアクセス
        target_url = 'https://www.shuwasystem.co.jp/book/9784798068596.html'
        driver.get(target_url)

        # 待機
        time.sleep(3)

        # データ抽出
        result = dict()
        result["title"] = driver.find_element(By.CLASS_NAME, "titleWrap").text
        result["author"] = driver.find_element(By.CSS_SELECTOR, "#main > div.detail > div.right > table > tbody > tr:nth-child(1) > td > a").text
        result["price"] = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[6]/td').text
        result['discribe'] = driver.find_element(By.ID, "bookSample").text
        result["title"] = driver.find_element(By.CLASS_NAME, "titleWrap").text

        # 出力確認
        print(result)
    finally:
        # ブラウザを閉じる
        driver.quit()
