# CoinBaseCryptoBot
Trading Bot used to trade Crypto currencies using the CoinBase API
It is based off the CoinBase Digital API [CoinBase API](https://developers.coinbase.com/)
**I am not responsible for the use or modification of this API/bot, by using this API/bot you agree that you are solely responsible for your actions and for your use of the API/bot.**
The bot is a work in progress.
## Requirements
- Python 3.x
- Coinbase
## Installation
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`  
`python3 get-pip.py`  
`pip install coinbase`
## Import
Store API key & secret from data.py file
`from data import api_key, api_secret`  
data.py:  
`api_key = "exampleapi"`  
`api_secret = "examplesecret"`  
## Usage
The bot uses the **ticker** of the Crypto e.g. BTC = BitCoin  
Set the currency of the Crypto e.g. 'USD'
`purchase(0.5, "BTC")`
#### Get information on a Crypto
`get_spot_price`
#### Buy a Crypto
`buy_price.amount`
#### Sell a Crypto
`sell_price.amount`