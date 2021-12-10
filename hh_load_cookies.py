from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

driver = webdriver.Chrome()
driver.get('https://www.hh.ru/')

for cookies in pickle.load(open('hh_session', 'rb')):
    driver.add_cookie(cookies)
driver.refresh()

driver.get('https://hh.ru/employer/5599')

