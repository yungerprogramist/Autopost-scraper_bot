import telebot 
from handler import main
from time import sleep

from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot (os.getenv('BOT_TOKEN')) 
chanel_id = '@sndfbnerkbvkd'


@bot.message_handler(commands=['start'])
def start(message):
    print('works')
    while True:
        all_posts = main()
        for post in all_posts:
            if 'Error' in post:
                continue 
            else:
                bot.send_message(chat_id=chanel_id, text = post ) #, parse_mode= "Markdown"


        sleep(1800)



if __name__ == '__main__':
    bot.infinity_polling()