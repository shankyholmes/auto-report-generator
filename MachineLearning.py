import pandas as pd
from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import units
from asammdf import mdf
from tkinter import filedialog

def csv_inp():
    folder = filedialog.askdirectory(title = 'select folder')
    files = [f for f in listdir(folder) if isfile(join(folder, f)) and f.endswith('.DAT')]
    
    return files

def read_table(filename):
    df = pd.read_table(filename, header = 2, sep = '\t')
    df = df.dropna(axis = 1)
    df = df.tail(-2)
    for cols in df.columns:
        try:
            df[cols] = df[cols].astype(float)
        except:
            continue
        finally:
            print("Data parse completed.")
    
    return df
    print(df.head())


filename = "D:\Designing\Programming\PyCharm\MachineLearning\AsciiTest.ascii"

df1 = read_table(filename)



df1 = df1[df1['Epm_nEng\CCP:2'] > 850]


def report_gen(c):
    c.translate(units.inch, units.inch)
    c.setFont("Helvetica", 24)
    c.drawCentredString(0, 0, "Hello World")


c = canvas.Canvas("TestPdf.pdf", pagesize = A4, bottomup = 0)
report_gen(c)
c.showPage()
c.save()

# eng = sns.distplot(df1['Epm_nEng\CCP:2'], bins = 100)
# uel = sns.distplot(df1['InjCrv_qSetUnBal\CCP:2'], bins = 100)
# sns.scatterplot(df1['Epm_nEng\CCP:2'], df1['InjCrv_qSetUnBal\CCP:2'])
