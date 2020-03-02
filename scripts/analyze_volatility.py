
# # # # # # # # # # #
#   I M P O R T S   #
# # # # # # # # # # #

from __future__ import division

import sys      # for command line arguments
import os       # for manipulating files and folders
import argparse # for command line arguments

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############
####metrics####
###############

def get_metrics(moving_wallets, prices):

    moving_wallets, prices = equal_lengths(moving_wallets, prices)

    drawdown = get_max_drawdown(moving_wallets)
    price_drawdown = get_max_drawdown(get_market_returns(prices))
    relative_drawdown = drawdown/price_drawdown

    beta = get_beta(moving_wallets, prices)
    deviation, rv = get_relative_volatility(moving_wallets, prices)

    sharpe = get_ratio(moving_wallets, prices)

    print("Beta: " + str(beta))
    print("Max Drawdown: " + str(drawdown))
    print("Relative Drawdown: " + str(relative_drawdown))
    print("Sharpe Ratio: " + str(sharpe))
    print("Relative Volatilty: " + str(rv))

    return [sharpe, drawdown, relative_drawdown, deviation, rv, beta]

def get_relative_volatility(moving_wallets, prices):

    market = get_market_returns(prices)
    market_variance = np.std(market)
    index_variance = np.std(moving_wallets)

    #plt.plot(market, label='Market Returns')
    #plt.plot(moving_wallets, label='Algo Returns')

    #plt.xlabel('2/11/2019 - 1/15/2020')
    #plt.ylabel('Returns')
    #plt.title('Algo vs Market')

    #plt.legend()
    #plt.show()

    print(market_variance)
    print(index_variance)

    relative_volatility = index_variance/market_variance

    return index_variance, relative_volatility

def get_ratio(moving_wallets, prices):

    moving_wallets[:] = [moving_wallet - 100 for moving_wallet in moving_wallets]

    stddev = np.std(moving_wallets)

    sharpe_ratio = moving_wallets[len(moving_wallets)-1] / stddev

    return sharpe_ratio

def get_max_drawdown(moving_wallets):

    drawdown = 0

    i = np.argmax(np.maximum.accumulate(moving_wallets) - moving_wallets) # end of the period

    if len(moving_wallets[:i]) > 0:

        j = np.argmax(moving_wallets[:i]) # start of period

        drawdown = (moving_wallets[j] - moving_wallets[i]) / moving_wallets[j]

    return np.round(drawdown*100, 2)

def get_beta(moving_wallets, prices):

    #stddev = np.std(moving_wallets)
    #print(stddev)

    market_returns, relative_performances = [], []

    for i in range(0, len(prices) - 1, 1):

        #returns:
        #market = (prices[i] / prices[0]) - 1.0
        #relative_performance = (moving_wallets[i] / 100) - 1.0

        #performance and relative performance
        #market = (prices[i] / prices[0])
        #relative_performance = ((moving_wallets[i] / 100) / market)

        #excess performance
        market = (prices[i] / prices[0])
        relative_performance = ((moving_wallets[i] / 100) - market)

        market_returns.append(market)
        relative_performances.append(relative_performance)

    #print(market_returns[len(market_returns)-1])
    #print(relative_performances[len(relative_performances)-1])

    covariance = np.cov(market_returns, relative_performances, bias=True)[0][1]
    #covariance = np.cov(market_returns, relative_performances)[0][1]
    market_variance = np.var(market_returns)
    beta = covariance / market_variance

    #print(covariance)
    #print(market_variance)
    #print(beta)

    return beta

def get_market_returns(prices):

    market_returns = []

    for i in range(0, len(prices) - 1, 1):

        market = (prices[i] / prices[0]) * 100
        market_returns.append(market)

    return market_returns

def equal_lengths(moving_wallets, prices):

    if len(moving_wallets) > len(prices):
        moving_wallets = moving_wallets[0:len(prices)]
    else:
        prices = prices[0:len(moving_wallets)]

    return moving_wallets, prices
