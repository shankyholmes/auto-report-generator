import wx
import os
import pandas as pd
import MDFFileHandler as mdf
import ReportGenerator as rp


def MyFrame(title):
    f = wx.Frame(None, title = title, size = (320, 150))
    mainSizer = wx.BoxSizer(wx.HORIZONTAL)
    grid = wx.GridBagSizer(hgap = 10, vgap = 10)
    selDatFile = wx.Button(f, id = 1, label = 'Select .dat', name = 'Select', pos = (10, 10))
    processDatFile = wx.Button(f, id = 2, label = 'Process File', name = 'Process', pos = (200, 10))
    genReport = wx.Button(f, id = 3, label = 'Gen report', name = 'Report', pos = (105, 60))
    f.Bind(wx.EVT_BUTTON, SelectDatFile, selDatFile)
    f.Bind(wx.EVT_BUTTON, ProcessDatFile, processDatFile)
    f.Bind(wx.EVT_BUTTON, GenerateReport, genReport)
    f.Show(True)


def SelectDatFile(event):
    dlg = wx.FileDialog(None, 'Select a .Dat file', '', '', '*.*', wx.FD_OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        filename = dlg.GetFilename()
        global dirname
        dirname = dlg.GetDirectory()
        global fileDir
        fileDir = os.path.join(dirname, filename)
        dlg.Destroy()
    else:
        event.Skip()


def ProcessDatFile(event):
    try:
        global datafiltered
        datafiltered = mdf.filtered_data(fileDir)
        datafiltered.to_csv(os.path.join(dirname, 'sortedList.csv'))
        print(dirname)
    except:
        print('Select correct file')
    finally:
        event.Skip()


def GenerateReport(event):
    try:
        rp.generate(datafiltered)
        print('Successful!')
    except:
        print('Report gen unsuccessful')
    finally:
        event.Skip()


app = wx.App(False)
frame = MyFrame('Auto Report Gen')
app.MainLoop()
