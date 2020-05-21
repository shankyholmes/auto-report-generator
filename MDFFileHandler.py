from os.path import join
import os
from asammdf import MDF
import pandas as pd
from fuzzywuzzy import process
import numpy as np


def csv_reader():
    file = join(os.path.dirname(__file__), 'signals_to_keep.csv')
    csv_df = pd.read_csv(file)
    csv_df = csv_df['to_keep'].tolist()
    return csv_df


def dat_reader(fileDir):
    file = fileDir
    # file = 'D:\Designing\Programming\PyCharm\MachineLearning\Test.dat'
    mdf_df = MDF(file)
    return mdf_df


def filtered_data(fileDir):
    csvLST = csv_reader()
    datDF = dat_reader(fileDir).to_dataframe()
    columns = datDF.columns
    df = pd.DataFrame()
    
    for col in csvLST:
        best_match = process.extractOne(col, columns)
        best_match_col = best_match[0]
        df = df.append(datDF[best_match_col])
    df = df.transpose()
    
    df_index = pd.date_range('1/1/2020', periods = len(df), freq = 'T', name = 'DateTimeIndex')
    df.set_index(df_index, False, inplace = True)
    df_resampled = df.resample('10T').asfreq()
    df_new_index = np.arange(0, len(df_resampled) / 10, 0.1)
    # print(df_new_index)
    # df_new_index = pd.period_range('1/1/2020', periods = len(df_resampled), freq = '0.1S', name = 'index')
    df_resampled.set_index(df_new_index, False, inplace = True)
    # print(df_resampled)
    return df_resampled


# fileDir = 'D:\Designing\Programming\PyCharm\MachineLearning\Test.dat'
# df = filtered_data(fileDir)
