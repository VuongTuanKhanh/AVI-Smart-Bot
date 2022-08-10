import re
import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_selenium():
    sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # browser = webdriver.Chrome('./chromedriver')
    browser = webdriver.Chrome('./chromedriver', options=chrome_options)
    browser.get("https://fpt.workplace.com/groups/1711052639163719")
