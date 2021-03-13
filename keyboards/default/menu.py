from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cryptomenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bitcoin')
        ],
        [
            KeyboardButton(text='Ethereum')
        ],
        [
            KeyboardButton(text='NFT')
        ]
    ]
)