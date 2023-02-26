"""
Title   : スクレイピング＆クローリングデータ収集
Section : 4 趣味に活かす情報収集偏
Theme   : 4 食べログの飲食店データを取得する）
Date    : 2023/2/26
Page    : P76 - P83
"""


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


SLEEP_TIME = 4
BASE_URL = "https://tabelog.com/tokyo/rstLst/?vs=1&sa=%E6%9D%B1%E4%BA%AC%E9%83%BD&sk=%25E5%2588%2580%25E5%2589%258A%25E9%25BA%25BA&lid=top_navi1&vac_net=&svd=20220822&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC03&LstCatD=RC0304&LstCatSD=RC030402&cat_sk=%E5%88%80%E5%89%8A%E9%BA%BA"
CSV_NAME = "sec4_hobby/output/04_tabelog.csv"


def get_page_num(driver):
    count_elements = driver.find_elements(By.CLASS_NAME, "c-page-count__num")
    paging_num = int(count_elements[1].text)
    total_num = int(count_elements[2].text)
    return total_num // paging_num


def get_store_url(driver):
    store_elements = driver.find_elements(By.CSS_SELECTOR, ".list-rst__wrap.js-open-new-window")
    store_elements = [i.find_element(By.TAG_NAME, "h3") for i in store_elements]
    store_elements = [i.find_element(By.TAG_NAME, "a") for i in store_elements]
    return [i.get_attribute("href") for i in store_elements]


def get_next(driver):
    pagenation_element = driver.find_elements(By.CLASS_NAME, "c-pagination__list")[-1]
    pagenation_element.find_element(By.TAG_NAME, "a").click()


def get_store_info(driver, url):
    # 地図のURLに移動
    map_url= url + "dtlmap/"
    driver.get(map_url)
    time.sleep(SLEEP_TIME)

    # データ取得
    # --- 辞書に変換して出力
    table_elements = driver.find_element(By.CSS_SELECTOR, ".c-table.c-table--form.rstinfo-table__table")
    th_texts = [i.text for i in table_elements.find_elements(By.TAG_NAME, "th")]
    td_texts = [i.text for i in table_elements.find_elements(By.TAG_NAME, "td")]
    return {k: v for k, v in zip(th_texts, td_texts)}


if __name__ == "__main__":
    try:
        # ドライバーの取得
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # URLにアクセス＆スリープ
        driver.get(BASE_URL)
        time.sleep(SLEEP_TIME)

        # ページ番号の取得
        # --- ページが多いので実際は1ページ目のみ
        page_num = get_page_num(driver)
        page_num = 1

        # URLの格納用
        store_urls = list()

        # URL取得
        # i = range(page_num)[0]
        for i in range(page_num):

            # URLの取得
            urls = get_store_url(driver)
            store_urls.extend(urls)

            # ページ遷移
            get_next(driver)
            time.sleep(SLEEP_TIME)

        # データ取得準備
        store_urls = store_urls[:2]
        result = list()

        # データ取得
        # i_url = store_urls[0]
        for i_url in store_urls:
            store_info = get_store_info(driver=driver, url=i_url)
            result.append(store_info)

        # データ出力
        df = pd.DataFrame(result)
        df.to_csv(CSV_NAME, index=False)

    finally:
        driver.quit()
