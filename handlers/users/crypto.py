from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

btc = cg.get_price(ids='bitcoin', vs_currencies=['usd', 'rub'])
btc_key = btc.get('bitcoin')
btc_reformat_usd = btc_key.get('usd')
btc_reformat_rub = btc_key.get('rub')


eth = cg.get_price(ids='ethereum', vs_currencies=['usd', 'rub'])
eth_key = eth.get('ethereum')
eth_reformat_usd = eth_key.get('usd')
eth_reformat_rub = eth_key.get('rub')

nft = cg.get_price(ids='nft-protocol', vs_currencies=['usd', 'rub'])
nft_key = nft.get('nft-protocol')
nft_reformat_usd = nft_key.get('usd')
nft_reformat_rub = nft_key.get('rub')
