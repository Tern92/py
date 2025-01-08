import telebot
from telebot import types
import random
token='7929920255:AAEmEHm11z7OfaSL9MODyu0TMd_oYZd3nGE'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    #markup = types.ReplyKeyboardMarkup(row_width=3)
    bot.reply_to(message, "Привет! Ты попал на игру - камень, ножницы, бумага:")

@bot.message_handler(func=lambda message: True)
def play_game(message):
    pchoise = message.text
    bchoise = random.choice(['Камень', 'Ножницы', 'Бумага'])

    if pchoise not in ['Камень', 'Ножницы', 'Бумага']:
        bot.send_message(message.id, "1")