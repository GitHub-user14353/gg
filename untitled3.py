# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxaIjhFTZjzilZH6vA-Ll2u65h_4Y6RN
"""

J = input()
if J == 'I':
  print("Заблокированно")
elif J == 'O':
  W = input("Выберите действие")
  if W == 'Remove':
    input('Какой файл удалить? ')
    print('Файл удален')
  elif W == 'Open':
    input('Какой файл открыть? ')
    print('*открывает файл*')
elif J == "E":
  S = input("Выберите действие: ")
  if S == 'Create':
    T = input('Имя файла: ')
    print('Создан файл ' + T)
  elif S == 'Remove':
    input('Какой файл удалить? ')
    print('Файл удален')
  elif S == 'Open':
    input('Какой файл открыть? ')
    print('*открывает файл*')
  elif S == 'Edit':
    input('Какой файл редактировать? ')
    print('*открывает файл для редактирования*')

def suit_function(elem: list):
  return 'a' in elem or "A" in elem

def filter_by(suit_function, this_list: list):
    new_list = []
    for element in this_list:
        if suit_function(element):
            new_list.append(element)
    
    return new_list

print(filter_by(suit_function,('ared','dg')))

import telebot
import requests
import json

bot = telebot.TeleBot("5486332535:AAG3wxpA21dM9OwzfomRbmhhkiuX3u1qqfE")
name = None
@bot.message_handler(commands=['start'])
def send_message(m):
  markup = telebot.types.ReplyKeyboardMarkup()\
      .add(telebot.types.KeyboardButton('/joke'))

  bot.send_message(
      m.chat.id,
      'Нажмите на кнопку, чтобы я отправил вам шутку')

bot.infinity_polling()