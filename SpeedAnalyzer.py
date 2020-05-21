import MDFFileHandler
# import seaborn as sns
from fuzzywuzzy import process
from ReportGenerator import reportGen
from scipy import stats
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, SimpleRNN
from sklearn.preprocessing import minmax_scale
import sklearn as skl
from scipy.signal import upfirdn


# df = MDFFileHandler.filtered_data('D:\Designing\Programming\PyCharm\MachineLearning\ArjunRotavator.dat')
# print(df.shape)
#
# # TRIM DATA AT BOTH ENDS
# PERCENT_TRUNCATION = 0.05
#
# no_rows = int(len(df) * PERCENT_TRUNCATION)
# df = df.tail(-no_rows)
# df = df.head(-no_rows)
#
#
# # df.to_csv('Truncated.csv')
# print(df.shape)
#
# df1 = reportGen.outlierTreatmentIQR(reportGen, df, 'Zscore')
#
# QSET = process.extractOne('InjCtl_qSetUnBal', df.columns)[0]
# SPEED = process.extractOne('Epm_nEng', df.columns)[0]
#
# grad = np.gradient(df[SPEED])
# grad = pd.DataFrame(data = grad)
# # print(grad)


df = pd.read_csv('Truncated.csv', index_col = [0])
print(df.shape)
df_index = pd.date_range('1/1/2020', periods = len(df), freq = 'T', name = 'DateTimeIndex')
df.set_index(df_index, False, inplace = True)
df_resampled = df.resample('10T').asfreq()
print(df_resampled)









(x_train, y_train) = tf.split()


model = Sequential()

model.add(LSTM(128, activation = 'relu', return_sequences = "True"))
