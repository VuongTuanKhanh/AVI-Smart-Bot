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

        from time import sleep

        pip_install('selenium')
        run_shell('apt-get update')

        sleep(10)

        apt_install('chromium-chromedriver')

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

    def login_workplace(self, username='', password=''):
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

            self.browser.find_element(
                By.ID, "login_password_submit_button").click()
            sleep(self.wait_time)
            self.browser.find_element(
                By.CSS_SELECTOR, '[name="email"]').send_keys(username)
            sleep(self.wait_time)
            self.browser.find_element(
                By.CSS_SELECTOR, '[type="submit"]').click()
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

    def scroll(self, times=0, wait=0):
        for i in range(times):
            self.browser.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            sleep(wait)

    def see_more(self):
        """Click on the 'See more' button
        """

        self.browser.execute_script('''
            for(let element of document.querySelectorAll('div[role="button"][class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"]')) 
            {
                element.click()
                await new Promise(r => setTimeout(r, 1000));
            }
        ''')

    def get_text(self):
        """Get the text of the current page
        """

        return self.browser.execute_script('''
            let results = []

            let feeds = document.getElementsByClassName("du4w35lb k4urcfbm l9j0dhe7 sjgh65i0")
            for (let feed of feeds)
            {
                let id = feed.querySelector('a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"').getAttribute('href').split('/')[6]
                
                let answers = []
                
                feed_question = feed.querySelector('div[class="dati1w0a ihqw7lf3 hv4rvrfc ecm0bbzt"]')
                feed_answers = feed.querySelectorAll('div[class="ecm0bbzt e5nlhep0 a8c37x1j"]')
                try {
                    question = feed_question.innerText
                }
                catch { 
                    continue
                }
                for (let answer of feed_answers) {
                    try {
                        data = answer.innerText
                    }
                    catch {
                        continue
                    }
                    answers.push(data)
                }
                results.push({
                    id: id,
                    question: question,
                    answers: answers
                })
            }
            return results
        ''')

    def crawl_data(self):
        self.see_more()
        self.data = self.get_text()

    def close(self):
        """Close the browser
        """

        self.browser.close()

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
