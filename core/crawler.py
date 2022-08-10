import re
import sys
from core.helper import *
from time import sleep


class Crawler():
    def __init__(self, framework='selenium', copy_from='../../usr/lib/chromium-browser/chromedriver', copy_to='../../usr/bin'):
        """Initialize the Crawler class

        Args:
            framework (str, optional): Framework used to crawl. Defaults to 'selenium'.
            copy_from (str, optional): Original Path. Defaults to '/usr/lib/chromium-browser/chromedriver'.
            copy_to (str, optional): Destination_path. Defaults to '/usr/bin'.
        """

        pip_install('selenium')
        run_shell('apt-get update')

        pip_install('chromedriver-py')
        # apt_install('chromium-chromedriver')

        # sys.path.insert(0, '../../usr/lib/chromium-browser/chromedriver')

    def get_browser(self):
        """Open a browser and go to the url
        Args:
            url (str): A specific url that need to be open in the browser
        """

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from chromedriver_py import binary_path

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        service_object = Service(binary_path)
        driver = webdriver.Chrome(
            '../../usr/local/lib/python3.7/dist-packages/chromedriver_py/chromedriver_linux64', options=chrome_options)

        return driver
