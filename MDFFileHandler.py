from os.path import join
import os
from asammdf import MDF
import pandas as pd
from fuzzywuzzy import process


def csv_reader():
    file = join(os.path.dirname(__file__), 'signals_to_keep.csv')
    csv_df = pd.read_csv(file)
    csv_df = csv_df['to_keep'].tolist()
    return csv_df

def dat_reader(fileDir):
    file = fileDir
    #file = 'D:\Designing\Programming\PyCharm\MachineLearning\Test.dat'
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
    return df

#data = filtered_data()

