#     file: simulate_db.py
#   author: Dan Healy
#  created: 6/19/2018
# modified: 6/19/2018
#  purpose: simulates buys and sells using predicted objective value to evaluate performance

# # # # # # # # # # #
#   I M P O R T S   #
# # # # # # # # # # #

import sys      # for command line arguments
import os       # for manipulating files and folders
import argparse # for command line arguments

import pandas as pd
import numpy as np
from datetime import datetime

import wallet_helper

# # # # # # # # # # # # #
#   C O N S T A N T S   #
# # # # # # # # # # # # #

DEF_BUY_SELL_PENALTY = 0.01 # 1% buy fee. 1% sell fee

# # # # # # # # # # # # #
#   F U N C T I O N S   #
# # # # # # # # # # # # #
def simulate_fixed_threshold(preds, times, price, buy = 1, sell = 0, is_invested = False, verbose = True):

    bp, wallet, ii, lt, is_invested_array, moving_wallets, adjusted_preds, expected_prices = simulate(preds, times, price, buy, sell, 0, 100, is_invested, verbose)

    if ii:
        wallet = wallet_helper.final_wallet(wallet, bp, price)

    return wallet, ii, lt, moving_wallets, adjusted_preds, is_invested_array, expected_prices

def simulate(preds, times, price, buy_thresh = 1, sell_thresh = 0, buy_price = 0, wallet = 100, is_invested = False, verbose = False):

    last_price, last_frame, sell_price = 0, 0, 0

    trade_strings, is_invested_array, expected_prices = [], [], []
    moving_wallets, fixed_wallets = [100], [100]

    for i in range(len(preds)):

        adjusted_pred = preds[i]

        if is_invested:
            current_wallet = fixed_wallets[len(fixed_wallets)-1] * (price[i] / buy_price)
            moving_wallets.append(current_wallet)
        else:
            moving_wallets.append(fixed_wallets[len(fixed_wallets)-1])

        if not is_invested and wallet_helper.should_buy(preds, i, buy_thresh):

            is_invested = True
            buy_price = price[i]
            last_price = buy_price
            last_frame = i

            trade_string = "Buy at " + str(price[i]) + " on " +  str(datetime.fromtimestamp(times[i]/1000.0))

            if verbose:
                print(trade_string)

            trade_strings.append(trade_string)

        elif is_invested and wallet_helper.should_sell(preds, i, sell_thresh):

            is_invested = False
            sell_price = price[i]
            last_price = sell_price
            last_frame = i

            trade_string = "Sell at " + str(price[i]) + " on " +  str(datetime.fromtimestamp(times[i]/1000.0))

            if verbose:
                print(trade_string)

            trade_strings.append(trade_string)

            wallet = wallet_helper.update_wallet(wallet, buy_price, sell_price, DEF_BUY_SELL_PENALTY)
            fixed_wallets.append(wallet)

        is_invested_array.append(is_invested)

    lt = ","

    if len(trade_strings) > 0:
        lt = lt.join(trade_strings)

    if not is_invested:
        buy_price = sell_price

    return buy_price, wallet, is_invested, lt, is_invested_array, moving_wallets, adjusted_preds, expected_prices
