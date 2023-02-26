"""
Title   : スクレイピング＆クローリングデータ収集
Section : 3 スクレイピングの実習
Theme   : 5 秀和システムのデータを取得する（縮小版）
Date    : 2023/2/26
Page    : P50 - P61
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# パラメータ設定
SLEEP_TIME = 5
CSV_NAME = "sec3_basic/output/syuwa.csv"


def update_num_page(driver, page_num):
    base_url = "https://www.shuwasystem.co.jp/search/index.php?search_genre=13273&c=1"
    page_option = f"&page={page_num}"
    next_url = base_url + page_option
    driver.get(next_url)


def get_item_urls(driver):
    ro_element = driver.find_element(By.CLASS_NAME, "bookWrap")
    ttl_elements = ro_element.find_elements(By.CLASS_NAME, "ttl")
    a_elements = [i.find_element(By.TAG_NAME, "a") for i in ttl_elements]
    return [i.get_attribute("href") for i in a_elements]


def is_last_page(driver):
    # 最後のページになると"次"の文字が消えることを利用する
    pagingWrap_element = driver.find_element(By.CLASS_NAME, "pagingWrap")
    paging_text = pagingWrap_element.find_element(By.CLASS_NAME, "right").text
    return not "次" in paging_text


def get_item_info(driver):
    result = dict()
    result["title"] = driver.find_element(By.CLASS_NAME, "titleWrap").text
    result["price"] = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[6]/td').text
    result["author"] = driver.find_element(By.CSS_SELECTOR,
                                           "#main > div.detail > div.right > table > tbody > tr:nth-child(1) > td").text
    result["describe"] = driver.find_element(By.ID, "bookSample").text
    return result


if __name__ == "__main__":
    try:
        # ドライバー指定
        driver = webdriver.Chrome(ChromeDriverManager().install())

        page_num = 1
        item_url = list()
        while True:
            # ページ遷移＆スリープ
            update_num_page(driver, page_num)
            time.sleep(SLEEP_TIME)
            # URLリストの作成
            urls = get_item_urls(driver)
            print(urls)
            item_url.extend(urls)
            if is_last_page(driver):
                break
            page_num += 1

        # データの量を減らす
        # --- 最初の2つのみ
        item_url = item_url[:2]

        item_infos = list()
        i_url = item_url[0]
        for i_url in item_url:
            driver.get(i_url)
            time.sleep(SLEEP_TIME)
            item_infos.append(get_item_info(driver))

        df = pd.DataFrame(item_infos)
        df.to_csv(CSV_NAME, index=False)

    finally:
        driver.quit()
