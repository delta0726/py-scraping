"""
Title   : スクレイピング＆クローリングデータ収集
Section : 4 趣味に活かす情報収集偏
Theme   : 3 Githubトレンドのデータを取得する
Date    : 2023/2/26
Page    : P65 - 70
"""


""" メモ： CSS_SELECTORの取得方法
＜コード＞
lang_elem = i_box.find_elements(By.CSS_SELECTOR, ".d-inline-block.ml-0.mr-3")

＜取得手順＞
1. Chromeで要素を選択する
2. 対象オブジェクトの1つ上のタグを取得 <span class="d-inline-block ml-0 mr-3">
3. classを空白をドットに変更して入力（先頭にもドットを付ける） 
"""


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SLEEP_TIME = 3
URL = "https://github.com/trending"
CSV_NAME = "sec4_hobby/output/03_github_trend.csv"


def extract_trend_data(driver):
    result = list()
    box_row_element = driver.find_elements(By.CLASS_NAME, "Box-row")

    # i_box = box_row_element[0]
    for i_box in box_row_element:
        row_data = dict()

        # Title
        title_elem = i_box.find_element(By.TAG_NAME, "h1")
        row_data["title"] = title_elem.text

        # Url
        url_elem = i_box.find_element(By.TAG_NAME, "h1").find_element(By.TAG_NAME, "a")
        row_data["url"] = url_elem.get_attribute("href")

        # Language
        lang_elem = i_box.find_elements(By.CSS_SELECTOR, ".d-inline-block.ml-0.mr-3")
        row_data["lang"] = lang_elem[0].text if len(lang_elem) == 1 else None

        # Total Star
        total_star_elem = i_box.find_elements(By.CSS_SELECTOR, ".Link--muted.d-inline-block.mr-3")
        row_data["total_star"] = total_star_elem[0].text

        # Fork
        fork_elem = i_box.find_elements(By.CSS_SELECTOR, ".Link--muted.d-inline-block.mr-3")
        row_data["fork"] = fork_elem[1].text

        # Today's star
        todays_star_elem = i_box.find_elements(By.CSS_SELECTOR, ".d-inline-block.float-sm-right")
        row_data["todays_star"] = todays_star_elem[0].text.replace("stars today", "").replace(" ", "")

        result.append(row_data)

    print(result)

    return pd.DataFrame(result)


if __name__ == "__main__":
    try:
        # ドライバー指定
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Webページにアクセス＆スリープ
        driver.get(URL)
        time.sleep(SLEEP_TIME)

        # データ取得＆保存
        df = extract_trend_data(driver)
        df.to_csv(CSV_NAME)

    finally:
        driver.quit()
