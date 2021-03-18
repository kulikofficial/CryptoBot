# -*- coding: utf-8 -*-
from pycoingecko import CoinGeckoAPI


def bitcoin():
    cg = CoinGeckoAPI()
    btc = cg.get_price(ids='bitcoin', vs_currencies=['usd', 'rub'])
    btc_key = btc.get('bitcoin')
    btc_reformat_usd = btc_key.get('usd')
    btc_reformat_rub = btc_key.get('rub')
    return f'<i>Bitcoin</i>\nUSD: 💲 <b>{btc_reformat_usd}</b>\nRUB: ₽ <b>{btc_reformat_rub}</b>'


def ethereum():
    cg = CoinGeckoAPI()
    eth = cg.get_price(ids='ethereum', vs_currencies=['usd', 'rub'])
    eth_key = eth.get('ethereum')
    eth_reformat_usd = eth_key.get('usd')
    eth_reformat_rub = eth_key.get('rub')
    return f'<i>Bitcoin</i>\nUSD: 💲 <b>{eth_reformat_usd}</b>\nRUB: ₽ <b>{eth_reformat_rub}</b>'


def nftprotocol():
    cg = CoinGeckoAPI()
    nft = cg.get_price(ids='nft-protocol', vs_currencies=['usd', 'rub'])
    nft_key = nft.get('nft-protocol')
    nft_reformat_usd = nft_key.get('usd')
    nft_reformat_rub = nft_key.get('rub')
    return f'<i>Bitcoin</i>\nUSD: 💲 <b>{nft_reformat_usd}</b>\nRUB: ₽ <b>{nft_reformat_rub}</b>'


def cardano():
    cg = CoinGeckoAPI()
    nft = cg.get_price(ids='cardano', vs_currencies=['usd', 'rub'])
    ada_key = nft.get('cardano')
    ada_reformat_usd = ada_key.get('usd')
    ada_reformat_rub = ada_key.get('rub')
    return f'<i>Cardano</i>\nUSD: 💲 <b>{ada_reformat_usd}</b>\nRUB: ₽ <b>{ada_reformat_rub}</b>'
