# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from pycoingecko import CoinGeckoAPI
from handlers.users.crypto import bitcoin, ethereum, nftprotocol, cardano
from keyboards.default import cryptomenu

from loader import dp

cg = CoinGeckoAPI()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=cryptomenu)


@dp.message_handler(text='Bitcoin')
async def get_bitcoin(message: types.Message):
    await message.answer(bitcoin())


@dp.message_handler(text='Ethereum')
async def get_bitcoin(message: types.Message):
    await message.answer(ethereum())


@dp.message_handler(text='NFT')
async def get_bitcoin(message: types.Message):
    await message.answer(nftprotocol())

@dp.message_handler(text='Cardano')
async def get_bitcoin(message: types.Message):
    await message.answer(cardano())
