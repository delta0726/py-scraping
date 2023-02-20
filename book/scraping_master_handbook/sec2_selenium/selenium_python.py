"""
Theme : Selenium Pythonの用意
Page  : 28
"""

from selenium import webdriver
from selenium.webdriver.chrome import service as fs


CHROME_DRIVER = "/usr/lib/chronmium-browser/chromedriver"

chrome_service = fs.Service(executable_path=CHROME_DRIVER)

driver = webdriver.Chrome(service=chrome_service)
