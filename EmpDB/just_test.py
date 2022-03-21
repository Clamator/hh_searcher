import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token



#app = Client('my_account1')

def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_news = soup.find_all('div', class_='feed__item l-island-round')
    first_new = main_news[0].find('a', class_='content-link').get('href')

    return first_new

def main():
    url = 'https://vc.ru/new'
    x = get_data(get_html(url))
    print(x)

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello')

    bot.polling()

if __name__ == '__main__':
    main()
    telegram_bot(token)