import re
import sys
from helper import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Crawler():
    def __init__(self, framework='selenium', copy_from='/usr/lib/chromium-browser/chromedriver', copy_to='/usr/bin'):
        """Initialize the Crawler class

        Args:
            framework (str, optional): Framework used to crawl. Defaults to 'selenium'.
            copy_from (str, optional): Original Path. Defaults to '/usr/lib/chromium-browser/chromedriver'.
            copy_to (str, optional): Destination_path. Defaults to '/usr/bin'.
        """
        
        import shutil
        
        pip_install('selenium')
        run_shell('apt-get update')
        run_shell('apt-get install chromium-browser')
        shutil.copy(copy_from, copy_to)
        
        sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

    def get_browser(self, url="https://fpt.workplace.com/groups/1711052639163719"):
        """Open a browser and go to the url
        Args:
            url (str): A specific url that need to be open in the browser
        """
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        browser = webdriver.Chrome('../../usr/bin/chromedriver',options=chrome_options)
        browser.get(url)
        return browser