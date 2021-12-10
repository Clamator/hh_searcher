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
        # option.headless = True
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(hh_login_page)

    # a function to login
    def login(self):
        for cookies in pickle.load(open('hh_session', 'rb')):
            self.driver.add_cookie(cookies)
        self.driver.refresh()
        sleep(0.5)

    # a function to search by some conditions
    def search(self):
        self.driver.get('https://hh.ru/search/vacancy/advanced')
        keywords = self.driver.find_element(By.ID, 'advancedsearchmainfield')
        keywords.send_keys('водитель')
        salary = self.driver.find_element(By.CSS_SELECTOR, 'input[class*="FormattedNumericInput-Visible"]')
        salary.send_keys('55000')
        full_employment = self.driver.find_element(By.NAME, 'employment')
        self.driver.execute_script("arguments[0].click();", full_employment)

        day_length = self.driver.find_element(By.XPATH, '//span[contains(text(), "Полный день")]')
        self.driver.execute_script("arguments[0].click();", day_length)
        period = self.driver.find_element(By.XPATH, '//span[contains(text(), "За месяц")]')
        self.driver.execute_script("arguments[0].click();", period)
        search_button = self.driver.find_element(By.ID, 'submit-bottom')
        self.driver.execute_script("arguments[0].click();", search_button)

    # a function to send respond
    def send_respond(self):
        all_vacancies = self.driver.find_elements(By.CSS_SELECTOR, 'div[class*="vacancy-serp-item"]')
        for sep_vacancy in all_vacancies:
            print(sep_vacancy.text)


if __name__ == '__main__':
    hh_login_page = 'https://hh.ru/account/login'
    hh_searcher = Headhunter()
    hh_searcher.login()
    hh_searcher.search()
    hh_searcher.send_respond()
