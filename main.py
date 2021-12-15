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
        #option.headless = True
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(hh_login_page)

    # a function to login
    def login(self):
        for cookies in pickle.load(open('hh_session', 'rb')):
            self.driver.add_cookie(cookies)
        self.driver.refresh()

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

    def write_csv(self, data):
        with open('hh_driver_results.csv', 'a', encoding='utf-8', newline='') as file:
            order = ['vacancy_name', 'company_name', 'contact_phone_number', 'contact_name', 'salary', 'address',
                     'respond_time']
            writer = csv.DictWriter(file, fieldnames=order)
            writer.writerow(data)

    # a function to parse data and send respond
    def send_respond(self):
        # here i get all the link of vacancies
        links_list = []
        for _ in range(10):
            all_vacancies = self.driver.find_elements(By.CLASS_NAME, 'vacancy-serp-item')
            for sep_vacancy in all_vacancies:
                try:
                    link = sep_vacancy.find_element(By.CSS_SELECTOR, 'a[class*="bloko-link"]').get_attribute('href')
                    # checking the uniqueness of link
                    if link not in links_list:
                        links_list.append(link)
                    else:
                        pass
                except:
                    print('no vacancy link')
            next_button = self.driver.find_element(By.XPATH, '//span[contains(text(), "дальше")]')
            self.driver.execute_script("arguments[0].click();", next_button)
        print(links_list)

        # here i parse data
        for test_link in links_list:
            test_button = self.driver.get(test_link)
            # the button below hits and opens employer contacts so I can parse it
            try:
                employer_contacts_button = self.driver.find_element(By.XPATH,
                                                                    '//span[contains(text(), "Контактная информация")]')
                self.driver.execute_script("arguments[0].click();", employer_contacts_button)
            except:
                continue
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

            respond_time = datetime.now()

            #try:
            #    respond_button = self.driver.find_element(By.CSS_SELECTOR, 'a[data-qa*="vacancy-response-link-top"]')
            #    self.driver.execute_script("arguments[0].click();", respond_button)
            #    sleep(5)
#
            #    hit_letter_button = self.driver.find_element(By.CSS_SELECTOR,
            #                                                 'span[data-qa*="vacancy-response-letter-toggle"]')
            #    self.driver.execute_script("arguments[0].click();", hit_letter_button)
            #    sleep(5)
            #    respond_text = self.driver.find_element(By.CSS_SELECTOR,
            #                                            'textarea[class*="bloko-textarea bloko-textarea_sized-rows"]')
            #    text = open('voditel.txt', 'r', encoding='utf-8')
            #    respond_text.send_keys(text.read())
            #    send_respond_text = self.driver.find_element(By.CSS_SELECTOR, 'button[type*="submit"]')
            #    sleep(5)
            #    self.driver.execute_script("arguments[0].click();", send_respond_text)
            #except:
            #    respond_button = 'button not found'

            data = {
                "vacancy_name": vacancy_name,
                "company_name": company_name,
                "contact_phone_number": contact_phone_number,
                "contact_name": contact_name,
                "salary": salary,
                "address": address,
                "respond_time": respond_time,
                #"respond_button": "yes" if respond_button != 'button not found' else 'no'
            }
            print(data)
            #self.write_csv(data)



if __name__ == '__main__':
    hh_login_page = 'https://hh.ru/account/login'
    hh_searcher = Headhunter()
    hh_searcher.login()
    hh_searcher.search()
    hh_searcher.send_respond()
