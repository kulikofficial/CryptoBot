# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import buy_callback

one_choice = InlineKeyboardMarkup(row_width=1)
surprise = InlineKeyboardMarkup(row_width=1)

click = InlineKeyboardButton(text="Нажимай на эту кнопку, там викторина", url='http://t.me/QuizBot?start=a3lWFYMs', callback_data=buy_callback.new(item_name="click"))
one_choice.insert(click)

surp = InlineKeyboardButton(text="Обещанный сюрприз",
                            callback_data=buy_callback.new(item_name="surprise"))
one_choice.insert(surp)

surp2 = InlineKeyboardButton(text="Обещанный сюрприз",
                            callback_data=buy_callback.new(item_name="surprise"))
surprise.insert(surp2)
