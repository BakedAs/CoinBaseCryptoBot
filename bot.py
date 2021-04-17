from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret
import logging

# https://developers.coinbase.com/docs/wallet/guides/buy-sell

# set up coinbase client with api keys
client = Client(api_key, api_secret)
# payment_method = client.get_payment_methods()[0] //USED TO GRAB PAYMENT ID TO ACTUALLY MAKE THE PURCHASE
# TODO:set up coinbase client without api keys (some api's don't require auth)
# api_url = https://api.coinbase.com/v2/

# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# globally set currency to use
currency_code = 'USD'
# funds available to purchase crypto with 
funds = 100000
# value of crypto stored in wallet
wallet = 0
# keep a log of all transactions
transaction_log = {}

# function to replicate the client.buy function provided by coinbase for testing
def purchase(amount, ticker):
    global funds
    global wallet
    global transaction_log
    response = {}
    curr_buy_price = (client.get_buy_price(currency=ticker))['amount']
    purchase_cost = amount * float(curr_buy_price)
    # build the response as JSON (python dict)
    response['funds_available'] = funds
    response['wallet_value'] = wallet
    response['purchase_price'] = (client.get_buy_price(currency=ticker))['amount']
    response['currency'] = ticker

    try:
        if purchase_cost < funds:
            funds = funds - purchase_cost
            wallet += amount
            response['current_funds'] = funds
            response['wallet_value'] = wallet
        else:
            logger.info('Transaction failed, not enough funds available')
            response['error'] = 'Transaction failed, not enough funds available'
            return (response)

    except ValueError:
        logger.info(ValueError)
        print(ValueError)
    transaction_log['transaction'] = response
    return response

response = purchase(1, currency_code)
response = purchase(0.5, currency_code)
response = purchase(0.3, currency_code)

full_transaction_log = transaction_log.items()
print(full_transaction_log)

# API's available: https://developers.coinbase.com/docs/wallet/guides/price-data
spot_price = client.get_spot_price(currency=currency_code)
print("Current Spot Price: $" + spot_price['amount'])

buy_price = client.get_buy_price(currency=currency_code)
print("Current Buy Price: $" + buy_price['amount'])

sell_price = client.get_sell_price(currency=currency_code)
print("Current Sell price: $" + sell_price['amount'])

# take user input
# user_limit_order = float(input("Enter a price for your Bitcoin limit order (USD): "))
# user_amount_spent = float(input("Enter how much you want to spend (USD): "))
# real transaction [DANGEROUS]:
# client.buy(amount=str(amount / float(curr_buy_price), currency=currency_code, payment_method=payment_method.id))

# reset currents and find percentage change
# buy_price = client.get_buy_price(currency=currency_code)

# TODO: define percentage change as separate function 
# percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)

# print bitcoin curent price, and percentage change
# print('Bitcoin is ' + str(buy_price.amount) + '\nPercent change in last 60 seconds: ' + format(percentage_gainloss, ".3f") + '%')

# within threshold
# if(float(buy_price.amount) <= user_limit_order):
    # buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount), currency=currency_code, payment_method=payment_method.id))
    # print("Bought $" + str(user_amount_spent) + " or " + str(user_amount_spent / float(buy_price.amount)) + " bitcoin at " + buy_price.amount)
