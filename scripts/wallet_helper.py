#     file: wallet_helper.py
#   author: Dan Healy
#  created: 7/3/2018
# modified: 7/3/2018
#  purpose: ...

from datetime import datetime

def final_wallet(wallet, buy_price, price):

    return wallet * price[len(price) - 1] / buy_price

def update_wallet(wallet, buy_price, sell_price, penalty):

    if buy_price == 0:
        buy_price = sell_price

    wallet *= (1.0 - penalty)
    wallet *= sell_price / buy_price
    wallet *= (1.0 - penalty)
    return round(wallet, 2)

def should_buy(preds, i, buy_thresh):
    if preds[i] > buy_thresh:
        return True
    return False

def should_sell(preds, i, sell_thresh):
    if preds[i] < sell_thresh:
        return True
    return False
