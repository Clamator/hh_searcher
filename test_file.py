from datetime import datetime
from multiprocessing import Pool
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
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
        for cookies in pickle.load(open('hh_session_inn', 'rb')):
            self.driver.add_cookie(cookies)
        self.driver.refresh()

    def send_respond(self):
        link = 'https://hh.ru/vacancy/49685757?from=vacancy_search_list&query=%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C'
        self.driver.get(link)
        try:
            employer_contacts_button = self.driver.find_element(By.XPATH,
                                                                '//span[contains(text(), "Контактная информация")]')
            self.driver.execute_script("arguments[0].click();", employer_contacts_button)
        except:
            pass
        try:
            vacancy_name = self.driver.find_element(By.CSS_SELECTOR, 'h1[class*="bloko-header-1"]').text.strip()
        except:
            vacancy_name = 'unknown vacancy name'
        try:
            salary = self.driver.find_element(By.CSS_SELECTOR, 'div[class*="vacancy-salary"]').text.strip()
        except:
            salary = 'by agreement'
        try:
            company_name = self.driver.find_element(By.CSS_SELECTOR,
                                                    'a[class*="vacancy-company-name"]').text.strip()
        except:
            company_name = 'unknown company name'
        try:
            contact_name = self.driver.find_element(By.CSS_SELECTOR,
                                                    'p[data-qa*="vacancy-contacts__fio"]').text.strip()
        except:
            contact_name = 'no contacts'
        try:
            contact_phone_number = self.driver.find_element(By.CSS_SELECTOR,
                                                            'p[data-qa*="vacancy-contacts__phone"]').text.strip()
            contact_phone_number = ''.join(x for x in contact_phone_number if x.isdigit() or x == '+')[:12]
        except:
            contact_phone_number = 'no contacts'
        try:
            address = self.driver.find_element(By.CSS_SELECTOR,
                                               'span[data-qa*="vacancy-view-raw-address"]').text.strip()
        except:
            address = 'address is unknown'

        try:
            respond_button = self.driver.find_element(By.CSS_SELECTOR, 'a[data-qa*="vacancy-response-link-top"]')
            self.driver.execute_script("arguments[0].click();", respond_button)
            sleep(5)

            hit_letter_button = self.driver.find_element(By.CSS_SELECTOR, 'span[data-qa*="vacancy-response-letter-toggle"]')
            self.driver.execute_script("arguments[0].click();", hit_letter_button)
            sleep(5)
            respond_text = self.driver.find_element(By.CSS_SELECTOR,
                                                    'textarea[class*="bloko-textarea bloko-textarea_sized-rows"]')
            text = open('voditel.txt', 'r', encoding='utf-8')
            respond_text.send_keys(text.read())
            send_respond_text = self.driver.find_element(By.CSS_SELECTOR, 'button[type*="submit"]')
            sleep(5)
            self.driver.execute_script("arguments[0].click();", send_respond_text)
        except:
            respond_button = 'button not found'

        respond_time = datetime.now()
        print(vacancy_name, salary, company_name, contact_name, contact_phone_number, address, respond_time, respond_button)


if __name__ == '__main__':
    hh_login_page = 'https://hh.ru/account/login'
    hh_searcher = Headhunter()
    hh_searcher.login()
    hh_searcher.send_respond()
