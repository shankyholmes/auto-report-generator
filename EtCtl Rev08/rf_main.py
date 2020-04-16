from os import listdir
from os.path import isfile, join
import os
from asammdf import MDF
from tkinter import filedialog
import pandas as pd


import i_var
import regen_csv as rc


def user_inp():
    k = input("Please Enter Output Document Title: ")
    return k


def csv_inp():
    folder = filedialog.askdirectory(title = 'select folder')
    return folder


def stage_fun(x):
    if x == b'Stage_0': return 0
    if x == b'Stage_1': return 1
    if x == b'Stage_2': return 2
    if x == b'Stage_3': return 3


def rf_fun():
    folder = filedialog.askdirectory(title = 'select folder')
    files = [f for f in listdir(folder) if isfile(join(folder, f)) and f.endswith('.DAT')]
    path = folder + "/csv"
    ctdf = pd.DataFrame(
        columns = ['FileName', 'Strt Count', 'End Count', 'mSot Strt', 'lSnce (kms)', 'mSot End', 'T5_Avg',
                   'ti_OnRoad(s)', 'ti(t5>550)(s)', 'ti(poi1>0)(s)', 'PoI1_a(mg)', 'PoI1_lts'])

    for f in files:
        yop = MDF(folder + '/' + f)
        obj = yop.filter(i_var.to_keep)
        df = obj.to_dataframe()
        headers = ['time'].append(i_var.to_keep)
        df.rename(columns = lambda x: x[0:len(x) - 7], inplace = True)
        df.reset_index(inplace = True)
        df3 = df['CoEOM_numStageActTSync']
        df3 = df3.apply(lambda x: stage_fun(x))
        df['CoEOM_numStageActTSync'] = df3
        try:
            os.mkdir(path)
        except OSError:
            print("---")
        ctdf = rc.r_csv(df, path, f, ctdf)
    print(ctdf)
    ctdf.to_csv('out.csv', header = True, index = False)
    return path
