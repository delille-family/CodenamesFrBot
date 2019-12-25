import os
import telebot
from dotenv import load_dotenv
from telebot import types
from words import pick_random_words, split_words_by_player
load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

wanna_play = 'Tu veux jouer à Codenames? pour commencer une partie envoie moi un chiffre entre 1 et 4'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup()
  for i in range(4):
    markup.add(str(i + 1))
  bot.reply_to(message, wanna_play, reply_markup=markup)

@bot.message_handler(regexp='^[1-4]$')
def echo_words(message):
  difficulty = int(message.text)
  words = pick_random_words(difficulty)
  words_by_player = [', '.join(x) for x in split_words_by_player(words)]
  message_1 = ', '.join(words)
  message_2 = 'joueur 1: {}\njoueur 2: {}\nmot interdit: {}'.format(*words_by_player)
  bot.reply_to(message, message_1)
  bot.reply_to(message, message_2)

bot.polling()
