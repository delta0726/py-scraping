"""
Theme : Seleniumにおけるブラウザのドライバーの用意
Page  : 28
"""

# ブラウザのドライバーの取得
# Selenium4 WebDriver の executable_path 使用に伴う警告の回避方法
# --- https://gammasoft.jp/blog/python-selenium-webdriver-deprecation-warning-by-executable_path/


from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


# パスを直接指定する
CHROME_DRIVER = "/usr/lib/chronmium-browser/chromedriver"
service = fs.Service(executable_path=CHROME_DRIVER)

# ドライバをインストールする
service = Service(ChromeDriverManager().install())

# ドライバーを実行
driver = webdriver.Chrome(service=service)
