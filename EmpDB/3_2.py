import time
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
import tgcrypto
import schedule


#app = Client('my_account1')

def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_data(html):
    soup = BeautifulSoup(html, 'html-parser')
    main_news = soup.find_all('div', class_='feed__item l-island-round')
    first_new = main_news[0].find('a', class_='content-link').get('href')

    return first_new



def send_message(txt):
    with open('config.ini', 'r') as file:
        data = file.readlines()
        ch2 = data[4].split(' = ')[1]
    with Client('my_account1') as app:
        app.send_message(ch2, txt)

    app.run()

def main():
    url = 'https://vc.ru/new'
    send_message(get_data(get_html(url)))

    #while True:
    #    schedule.run_pending()

if __name__ == '__main__':
    main()
