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

def simulate_all_variants(type, partition = None, strings = [], include_fixed = False, time_stamp = True):

    if strings == []:
        strings = ['pred', 'readjusted_index_unadjusted', 'index', 'readjusted_index']

    df_array, name_array = get_variants.get_all_variants(type, strings)

    active_wallet_array, relative_performances, stats, volatility_stats = [], [], [], []

    last_trades, moving_wallets, price_array, time_array, is_invested_arrays = [], [], [], [], []

    for i in range(0, len(df_array), 1):

        print("Current Index: " + str(df_array[i]['index'].values[len(df_array[i]['index'].values) - 1]))

        wallet, ii, lt, mw, adjusted_preds, is_invested_array, expected_prices = simulate_db.simulate_fixed_threshold(df_array[i]['index'].values, df_array[i]['times'].values, df_array[i]['price'].values, 1, 0, False, True)
        #prediction_performance.plot_arrays([mw])
        last_trades.append(lt)
        moving_wallets.append(mw)
        is_invested_arrays.append(is_invested_array)
        price_array.append(df_array[i]['price'].values)
        time_array.append(df_array[i]['times'].values)

        active_wallet_array.append(wallet)
        relative_performances.append(get_relative_performance(df_array[i], wallet))
        stats.append(analyze_simulation.trade_stats(lt))

def get_relative_performance(df, wallet):
    market = df['price'].values[len(df['price'].values) - 1] / df['price'].values[0]
    return wallet/(market*100)

simulate_all_variants("BTC")
