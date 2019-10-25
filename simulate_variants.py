#     file: simulate_variants.py
#   author: Dan Healy
#  created: 1/17/2018
# modified: 1/17/2018
#  purpose: simulate variants

# # # # # # # # # # #
#   I M P O R T S   #
# # # # # # # # # # #

import sys      # for command line arguments
import os       # for manipulating files and folders

import argparse # for command line arguments

import pandas as pd
import numpy as np
from datetime import datetime

import analyze_simulation
import get_variants
import simulate_db

def simulate_all_variants(partition = None, strings = [], include_fixed = False, time_stamp = True):

    if strings == []:
        strings = ['pred', 'readjusted_index_unadjusted', 'index', 'readjusted_index']

    df_array, name_array = get_variants.get_all_variants("BTC", strings)

    for i in range(0, len(df_array), 1):

        print("XXX")
        print(name_array[i])
        wallet, ii, lt, mw, adjusted_preds, is_invested_array, expected_prices = simulate_db.simulate_fixed_threshold(df_array[i]['index'].values, df_array[i]['times'].values, df_array[i]['price'].values, 1, 0, False, True)
        print("Wallet: " + str(wallet))
        #print("Relative Performance: " + str(get_relative_performance(df_array[i], wallet)))
        print("XXX")

        #Uncomment to see basic stats on simulation
        #analyze_simulation.trade_stats(lt)

def simulate_variant(name, string):

    df = get_variants.get_complete_variant("BTC", name, string)

    wallet, ii, lt, mw, ap, iia, ep = simulate_db.simulate_fixed_threshold(df['index'].values, df['times'].values, df['price'].values, 1, 0, False, True)
    print("Wallet: " + str(wallet))

    price = df['price'].values
    price = price / price[0]
    price = price * 100

    market = 100*(price[len(price)-1]/price[0])
    print("Market: " + str(market))

    print("Wallet/Market: " + str(wallet/market))

    return lt, df['price'].values, df['times'].values

def get_relative_performance(df, wallet):
    market = df['price'].values[len(df['price'].values) - 1] / df['price'].values[0]
    return wallet/(market*100)
