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
from datetime import datetime, timedelta

VARIANT_PATH = "/home/ec2-user/Birdcoin/data/db/variants/"
ALT_VARIANT_PATH = "/home/ec2-user/Birdcoin/data/variants/"
ALT_ALT_VARIANT_PATH = "/ec2-user/Birdcoin/data/variants/"

LOCAL_VARIANTS_PATH = './variants/'

def get_all_variants(type, strings = ['pred', 'readjusted_index_unadjusted', 'index', 'readjusted_index'], start_date = "2_9_2019", include_fixed = False):

    names = ['readjusted_average', 'readjusted_median', 'readjusted_average_index_3',
            'readjusted_median_index_3', 'readjusted_average_index_7', 'readjusted_median_index_7',
            'readjusted_median_index_8_offset', 'readjusted_average_index_8_offset']

    fixed_names = ['fixed_average', 'fixed_median', 'fixed_average_index_3',
            'fixed_median_index_3', 'fixed_average_index_7', 'fixed_median_index_7',
            'fixed_median_index_8_offset', 'fixed_average_index_8_offset']

    df_array, name_array = [], []

    for string in strings:

        for name in names:

            df = get_complete_variant(type, name, string, start_date)
            full_name = name + "_" + string
            df_array.append(df)
            name_array.append(full_name)

        if string == 'readjusted_index' and include_fixed == True:

            for name in fixed_names:

                df = get_complete_variant(type, name, string, start_date)
                full_name = name + "_" + string
                df_array.append(df)
                name_array.append(full_name)

    return df_array, name_array

def get_complete_variant(type, name, index_string, start_date = "2_9_2019", date = datetime.now()):

    date_string = date.strftime("%-m_%-d_%Y")

    frames = []

    ec2_path = ALT_ALT_VARIANT_PATH

    while date_string != start_date:
    #not inclusive of start date

        date = subtract_day(date)

        if date > datetime(2020, 1, 15):
            continue

        date_string = date.strftime("%-m_%-d_%Y")

        if date_string == "10_23_2019":
            ec2_path = ALT_VARIANT_PATH

        if date_string == "3_13_2019":
            ec2_path = VARIANT_PATH

        df = get_variant_df(type, name, index_string, date_string, ec2_path)
        frames.insert(0, df)

    return pd.concat(frames)

def get_variant_df(type, name, index_string, date, ec2_path):

    path = get_path(type, date, ec2_path) + get_filename(type, name, index_string, date)

    df = pd.DataFrame()

    if os.path.exists(path):
        df = pd.read_csv(path)

    return df

def subtract_day(date):
    day_minus_one = date - timedelta(1)
    return day_minus_one

def get_filename(type, name, index_string, date):
    return type + "_" + name + "_" + index_string + "_" + date + ".csv"

def get_path(type, date_string, ec2_path):
    return LOCAL_VARIANTS_PATH + type + "/" + date_string + ec2_path + type + "/"
