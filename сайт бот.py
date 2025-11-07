import telebot
import random
from telebot import types
import requests
import json
bot = telebot.TeleBot("8311876884:AAFBdeWsOsMRgV1amh7HWPfowY1brVUlvQs")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"привет ,{message.from_user.first_name}")
    bot.send_message(message.chat.id,"привет")
bot.polling()