
# # # # # # # # # # #
#   I M P O R T S   #
# # # # # # # # # # #

import sys      # for command line arguments
import os       # for manipulating files and folders

import argparse # for command line arguments

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.stats as stats

from datetime import datetime

import get_variants

def animate_ma(index_string, variant = '', ma_frames = 96*10, days_offset = 0, median = False):

    df = get_variants.get_complete_variant("BTC", variant, index_string, "2_9_2019")
    comparison, times, prices = df['index'].values, df['times'].values, df['price'].values

    mas = get_ma(comparison, ma_frames, median)
    #mas, prices, sentinel = adjust_arrays(mas, prices, ma_frames)

    if days_offset > 0:
        prices = prices[0:len(prices)-days_offset*96]
        mas = mas[0:len(mas)-days_offset*96]

    sentinel = 0

    animate_catch([mas, prices], sentinel, frame_rate = 100, normal = True)

####################
###charts/plots#####
####################

def plot_ma(index_string, variant = '', ma_frames = 96*10, days_offset = 0, median = False, adjust = 0):

    df = get_variants.get_complete_variant("BTC", variant, index_string)
    comparison, times, prices = df['index'].values, df['times'].values, df['price'].values

    pretty_print = True

    if not pretty_print:

        mas = get_ma(comparison, ma_frames, median) ##comment for one pager

        total_offset = days_offset * 96

        if total_offset > len(prices):
            days_offset = 0

        if days_offset > 0:
            prices = prices[0:len(prices)-total_offset]
            mas = mas[0:len(mas)-total_offset]
            times = times[0:len(mas)-total_offset]

        print(mas[len(mas)-1])
        print(comparison[len(comparison)-1])

        mas = normalize(mas, max(prices), min(prices))
        prices = prices[adjust*96:len(prices)]

    else:

        mas = get_ma(comparison, ma_frames, median)

        print(mas[len(mas)-1])
        print(comparison[len(comparison)-1])

        mas = mas[ma_frames:len(mas)-1]
        prices = prices[ma_frames:len(prices)-1]

        prices = prices[adjust*96:len(prices)]

        mas = normalize(mas, max(prices), min(prices))

    plt.plot(mas, label='Predicted Price')
    plt.plot(prices, label='Actual Price')

    plt.xlabel('4/2/2019 - 1/15/2020')
    plt.ylabel('Returns')
    plt.title('Predicted Price vs Actual Price')

    plt.legend()
    plt.show()

def adjust_arrays(mas, prices, ma_frames):

    bandwidth_offset = 12*96
    sentinel = ma_frames + bandwidth_offset
    prices = prices[sentinel:len(prices)]

    return mas, prices, sentinel

##############################
###correlate/scatterplot######
##############################

def correlate_ma(index_string, variant = '', ma_frames = 96*10, days_offset = 0, median = False, adjust = 0):

    df = get_variants.get_complete_variant("BTC", variant, index_string)
    comparison, times, prices = df['index'].values, df['times'].values, df['price'].values

    i=ma_frames

    mas = get_ma(comparison, i, median)
    mas = normalize(mas, max(prices), min(prices))

    mas = mas[i:len(mas)-1]
    new_prices = prices[i:len(prices)-1]

    mas = mas[0:len(mas)-adjust*96]
    new_prices = new_prices[adjust*96:len(prices)]

    slope, intercept, r_value, p_value, std_err = stats.linregress(mas, new_prices)
    rsq=r_value*r_value
    print(rsq)

    #r=stats.spearmanr(mas, new_prices)[0]
    #print(r*r)

    make_scatter(mas, new_prices)

def make_scatter(x, y, j = 0):

    #predicted, actual

    fig, ax = plt.subplots()

    ax.scatter(x, y, s = 1, c = 'blue', rasterized=True)

    m, b = np.polyfit(x, y, deg = 1)
    x0, x1 = ax.get_xlim()
    y0, y1 = m*x0+b, m*x1+b
    ax.plot([x0, x1], [y0, y1], c = 'black')

    plt.xlabel('Predicted Price')
    plt.ylabel('Actual Price')
    #Apr 2 is 50 days (default MA length) after set begins
    plt.title('Price vs Prediction, Apr 2 - Jan 15, R^2=.78')

    plt.show()

####################
######animate#######
####################

def animate_catch(array, sentinel = 0, frame_rate = 100, normal = True):

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)

    fig = plt.figure()

    def animate(i, array, sentinel):

        plt.clf()
        i = i*frame_rate

        fixed = array[0][0:i]
        animated = array[1][0:i - sentinel]

        if len(fixed) > 0 and len(animated) > 0:

            if normal:
                plt.plot(normalize(fixed, max(animated), min(animated)))
                #plt.plot(normalize(fixed))
            else:
                plt.plot(fixed)

            if i > sentinel:

                if normal:
                    plt.plot(animated)
                    #plt.plot(normalize(animated))
                else:
                    plt.plot(animated)

            plt.xlabel("Number of Periods")
            plt.ylabel("Price (USD)")
            plt.title("Price vs Prediction (10 Day Moving Average)")
            #plt.ylabel("Normalized Value from 0 to 1")
            #plt.title("Price vs Predictions 10 Day MA")

            plt.legend()
            #plt.plot(fixed)
            #plt.plot(animated)

    ani = animation.FuncAnimation(fig, animate, fargs = (array, sentinel,), frames = int(len(array[0]) / frame_rate), save_count = int(len(array[0]) / frame_rate), repeat=False)
    #ani.save(TAB_PATH + 'BTC_price_vs_preds_MA.mp4', writer=writer)
    plt.show()

##############
##getter#####
#############

def get_ma(array, interval = 96*10, median = False):

    mas = []

    for i in range(0, len(array), 1):

        sum = 0

        if i >= interval:

            if median:

                subarray = array[i-interval:i]
                median = np.median(subarray)
                mas.append(median)

            else:

                for j in range(i - interval, i, 1):
                    sum += array[j]

                average = sum / interval
                mas.append(average)

        else:
            mas.append(0)

    return mas

######normalize######

def normalize(x, new_max = 1, new_min = 0, length_of_lookback = 0):

    #return ((x - min(x) ) / (max(x) - min(x) ) * new_max) - downward_shift

    if length_of_lookback != 0 and len(x) > length_of_lookback:
        x = x[len(x)-length_of_lookback:len(x)]

    x = np.array(x)
    x = (new_max - new_min) / (max(x) - min(x)) * (x - max(x)) + new_max

    return x
