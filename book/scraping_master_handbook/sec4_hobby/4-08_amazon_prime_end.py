"""
Title   : スクレイピング＆クローリングデータ収集
Section : 4 趣味に活かす情報収集編
Theme   : 8 Amazonプライムビデオの配信終了作品の情報を取得する
Date    : 2023/03/02
Page    : P97 - P100
"""


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# パラメータ設定
SLEEP_TIME = 10
BASE_URL = "https://animephilia.net/amazon-prime-video-expiring-calendar/"
CSV_NAME = "sec4_hobby/output/08_amazon_prime_end.csv"


def get_info(driver):
    results_info = list()
    day_elements = driver.find_elements(By.CLASS_NAME, "day-column")

    # データ収集
    # i_day = day_elements[0]
    for i_day in day_elements:
        day_data = i_day.get_attribute("data-date")
        contents_elements = i_day.find_elements(By.CSS_SELECTOR, ".event.upcoming")
        # i_content = contents_elements[0]
        for i_content in contents_elements:
            result_contents = dict()
            result_contents["day"] = day_data
            result_contents["title"] = i_content.find_element(By.CLASS_NAME, "content-title").text
            result_contents["url"] = i_content.find_element(By.CLASS_NAME, "content-title").get_attribute("href")
            results_info.append(result_contents)
    return results_info


def calender_update(driver):
    driver.execute_script("window.scrollBy(0, 600);")
    driver.find_element(By.CLASS_NAME, "next").click()


if __name__ == "__main__":
    try:
        # ドライバーの取得
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # URLにアクセス&スリープ
        driver.get(BASE_URL)
        time.sleep(SLEEP_TIME)

        # データ取得
        results = list()
        for i in range(3):
            results.extend(get_info(driver))
            calender_update(driver)
            time.sleep(SLEEP_TIME)

        # データ保存
        pd.DataFrame(results).to_csv(CSV_NAME)

    finally:
        driver.quit()
