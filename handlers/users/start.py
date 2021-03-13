from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users.crypto import btc_reformat_usd, btc_reformat_rub, eth_reformat_usd, eth_reformat_rub, \
    nft_reformat_usd, nft_reformat_rub
from keyboards.default import cryptomenu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=cryptomenu)


@dp.message_handler(text='Bitcoin')
async def get_bitcoin(message: types.Message):
    await message.answer(f'<i>Bitcoin</i>\nUSD: 💲 <b>{btc_reformat_usd}</b>\nRUB: ₽ <b>{btc_reformat_rub}</b>')


@dp.message_handler(text='Ethereum')
async def get_bitcoin(message: types.Message):
    await message.answer(f'<i>Ethereum</i>\nUSD: 💲 <b>{eth_reformat_usd}</b>\nRUB: ₽ <b>{eth_reformat_rub}</b>')


@dp.message_handler(text='NFT')
async def get_bitcoin(message: types.Message):
    await message.answer(f'<i>NFT</i>\nUSD: 💲 <b>{nft_reformat_usd}</b>\nRUB: ₽ <b>{nft_reformat_rub}</b>')
