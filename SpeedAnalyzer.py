import MDFFileHandler
import seaborn as sns
from fuzzywuzzy import process
from ReportGenerator import reportGen
from scipy import stats
import pandas as pd
import numpy as np


df = MDFFileHandler.filtered_data('D:\Designing\Programming\PyCharm\MachineLearning\ArjunRotavator.dat')
print(df.shape)

# TRIM DATA AT BOTH ENDS
PERCENT_TRUNCATION = 0.05

no_rows = int(len(df) * PERCENT_TRUNCATION)
df = df.tail(-no_rows)
df = df.head(-no_rows)
print(df.shape)

df1 = reportGen.outlierTreatmentIQR(reportGen, df, 'Zscore')

QSET = process.extractOne('InjCtl_qSetUnBal', df.columns)[0]
SPEED = process.extractOne('Epm_nEng', df.columns)[0]

grad = np.gradient(df[SPEED])
grad = pd.DataFrame(data = grad)
# print(grad)


# s1 = sns.lineplot(df.index, df[SPEED])
# s2 = sns.lineplot(grad.index, grad.iloc[:, 0])

from random import randrange
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose

series = df[SPEED]
result = seasonal_decompose(series, model = 'multiplicative', period = 1)
result.plot()
pyplot.show()
