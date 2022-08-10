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


    def get_browser(self):
        """Open a browser and go to the url
        Args:
            url (str): A specific url that need to be open in the browser
        """

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.browser = webdriver.Chrome(
            '../../usr/bin/chromedriver', options=chrome_options)


    def get_url(self, url=''):
        """Open a browser and go to the url
        Args:
            url (str): A specific url that need to be open in the browser
        """

        if url:
            self.url = url
        self.browser.get(url)
        
        
    def login(self, username='', password=''):
        """Login to the website
        Args:
            username (str): Username of the user
            password (str): Password of the user
        """
        
        if not username:
            username = self.username
            
        if not password:
            password = self.password

        if self.url:
            from selenium.webdriver.common.by import By
            
            self.browser.find_element(By.ID, "login_password_submit_button").click()
            sleep(self.wait_time)
            self.browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(username)
            sleep(self.wait_time)
            self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
            sleep(2 * self.wait_time)
            self.browser.find_element(By.ID, "i0116").send_keys(self.username)
            sleep(self.wait_time)
            self.browser.find_element(By.ID, "idSIButton9").click()
            sleep(self.wait_time)
            self.browser.find_element(By.ID, "i0118").send_keys(password)
            sleep(self.wait_time)
            self.browser.find_element(By.ID, "idSIButton9").click()
            sleep(self.wait_time)
            self.browser.find_element(By.ID, "idSIButton9").click()
            sleep(self.wait_time)
        
        
    @property
    def username(self):
        return 'khanhvt3@fsoft.com.vn'
    
    
    @property
    def password(self):
        return 'LupusReginaAIEngineer16/11/1999'
    
    
    @property
    def wait_time(self):
        return 2
        
        
    def get_source(self):
        """Get the source of the current page
        """

        return self.browser.page_source
    
    
    def get_title(self):
        """Get the title of the current page
        """

        return self.browser.title
    
    
    def get_urls(self):
        """Get the urls of the current page
        """

        return self.browser.find_elements_by_tag_name('a')
    
    
    def get_urls_text(self):
        """Get the urls of the current page
        """

        return [url.text for url in self.get_urls()]
    
    
    def get_urls_href(self):
        """Get the urls of the current page
        """

        return [url.get_attribute('href') for url in self.get_urls()]