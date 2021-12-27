# from pandas.core import indexing
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
# from time import sleep
# import boto3
# import pandas as pd
# from datetime import datetime


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


chrome_options = set_chrome_options()
driver = webdriver.Chrome(options=chrome_options)
# Do stuff with your driver
url = 'https://www.basketball-reference.com/players/j/jamesle01.html'
driver.get(url)

meta = driver.find_element(By.ID, 'meta')
print(meta.text)

