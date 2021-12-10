from datetime import datetime, date, time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
import pickle
class Headhunter(object):

    def __init__(self):
        option = options = Options()
        option.add_argument("--disable-blink-features=AutomationControlled")
        #option.headless = True
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(hh_login_page)

    def login(self):
        for cookies in pickle.load(open('hh_session', 'rb')):
            self.driver.add_cookie(cookies)
        self.driver.refresh()
        sleep(0.5)

    def search(self):
        self.driver.get('https://hh.ru/search/vacancy/advanced')
        keywords = self.driver.find_element(By.ID, 'advancedsearchmainfield')
        keywords.send_keys('Python junior')


if __name__ == '__main__':
    hh_login_page = 'https://hh.ru/account/login'
    hh_searcher = Headhunter()
    hh_searcher.login()
    hh_searcher.search()
