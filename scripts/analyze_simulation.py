#     file: analyze_simulation.py
#   author: Dan Healy
#  created: 2/14/2018
# modified: 2/14/2018
#  purpose: analyze simulations

# # # # # # # # # # #
#   I M P O R T S   #
# # # # # # # # # # #

from __future__ import division

import sys      # for command line arguments
import os       # for manipulating files and folders
import argparse # for command line arguments

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from datetime import datetime

DEF_BUY_SELL_PENALTY = 0.01 # 1% buy fee. 1% sell fee

def parse_trade_details(lt):

    trades = []

    if lt == ',':
        return trades

    trade_strings = lt.split(",")

    for i in range(len(trade_strings)):

        trade = trade_strings[i].split(" ")

        price = float(trade[2])

        time = trade[4] + " " + trade[5]

        buy = False

        if trade[0] == "Buy":
            buy = True

        trades.append({"buy": buy, "price": price, "time": time})

    return trades

def last_bought(lt):
    trades = parse_trade_details(lt)
    if len(trades) == 0:
        return False
    return trades[len(trades)-1]["buy"]

def trade_stats(lt):

    trades = parse_trade_details(lt)

    buys, sells, fails, successes, successful_buys, successful_sells, failure_buys, failure_sells = [], [], [], [], [], [], [], []

    buy_success_mean, sells_success_mean, buy_failure_mean, sells_failure_mean = 0, 0, 0, 0

    for j in range(len(trades) - 1):

        change = (trades[j + 1]["price"] - trades[j]["price"])/trades[j]["price"]

        if trades[j]["buy"]:

            buys.append(change)

            if change > DEF_BUY_SELL_PENALTY:
                successful_buys.append(change)
                successes.append(change)
            else:
                failure_buys.append(change)
                fails.append(change)

        else:

            sells.append(change)

            if change < DEF_BUY_SELL_PENALTY * -1:
                successful_sells.append(change)
                successes.append(change)
            else:
                failure_sells.append(change)
                fails.append(change)

    buy_mean = np.mean(buys)
    sell_mean = np.mean(sells)

    if len(successful_buys) > 0:
        buy_success_mean = np.mean(successful_buys)

    if len(successful_sells) > 0:
        sells_success_mean = np.mean(successful_sells)

    if len(failure_buys) > 0:
        buy_failure_mean = np.mean(failure_buys)

    if len(failure_sells) > 0:
        sells_failure_mean = np.mean(failure_sells)

    print("Buy Mean: " + str(buy_mean))
    print("Sell Mean: " + str(sell_mean))

    print("Success Mean: " + str(np.mean(successes)))
    print("Failure Mean: " + str(np.mean(fails)))

    if len(buys) > 0 and len(sells) > 0:

        buys_success_rate = len(successful_buys) / len(buys)
        sells_success_rate = len(successful_sells) / len(sells)

        print("Buy Success Rate: " + str(buys_success_rate))
        print("Sell Success Rate: " + str(sells_success_rate))

    #print("Expected Value of Buy: " + str(buys_success_rate * buy_success_mean))
    #print("Expected Value of Sell: " + str(sells_success_rate * sells_success_mean))

    is_buy = False

    if len(trades) > 0:
        is_buy = trades[len(trades)-1]["buy"]

    print("XXX")

    return buys, sells, successes, fails, is_buy, successful_buys, failure_buys, successful_sells, failure_sells
