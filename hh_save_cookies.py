from selenium import webdriver
import pickle
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.hh.ru/login')

sleep(120)
pickle.dump(driver.get_cookies(), open('hh_session_inn', 'wb'))
driver.quit()