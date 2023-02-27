"""
Title   : スクレイピング＆クローリングデータ収集
Section : 4 趣味に活かす情報収集編
Theme   : 7 Amazonプライムビデオの配信作品の情報を取得する
Date    : 2023/02/28
Page    : P92 - P96
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# パラメータ設定
SLEEP_TIME = 10
BASE_URL = "https://animephilia.net/amazon-prime-video-arrival-calendar/"
CSV_NAME = "sec4_hobby/output/07_amazon_prime_start.csv"


def get_info(driver):
    results = list()
    day_elements = driver.find_elements(By.CLASS_NAME, "day-column")

    # i_day = day_elements[0]
    for i_day in day_elements:
        day_data = i_day.get_attribute("data-date")

        # コンテンツ・ボックスの取得
        # --- 修正：CSS_SELECTORが動作しないので、CLASS_NAMEに変更
        #content_elements = i_day.find_elements(By.CSS_SELECTOR, ".event.upcoming")
        content_elements = i_day.find_elements(By.CLASS_NAME, "content-title-box")

        # i_content = content_element[0]
        for i_content in content_elements:
            content_result = dict()
            content_title = i_content.find_element(By.CLASS_NAME, "content-title")
            content_result["day"] = day_data
            content_result["title"] = content_title.text
            content_result["url"] = content_title.get_attribute("href")
            results.append(content_result)

    return results


if __name__ == "__main__":
    try:
        # ドライバーの取得
        driver =webdriver.Chrome(ChromeDriverManager().install())

        # URLにアクセス&スリープ
        driver.get(BASE_URL)
        time.sleep(SLEEP_TIME)

        # データ取得
        result = get_info(driver)

        # データ保存
        pd.DataFrame(result).to_csv(CSV_NAME, index=False)

    finally:
        driver.quit()
