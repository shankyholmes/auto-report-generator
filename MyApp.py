import wx
import os
import MDFFileHandler as mdf
from ReportGenerator import reportGen

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((342, 258))
        self.datSelect = wx.Button(self, wx.ID_OPEN, "")
        self.datSelect_copy = wx.Button(self, wx.ID_ANY, "Generate")
        self.Status = self.CreateStatusBar(1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.SelectDatFile, self.datSelect)
        self.Bind(wx.EVT_BUTTON, self.GenerateReport, self.datSelect_copy)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Report Generator")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("D:\\Designing\\Programming\\PyCharm\\MachineLearning\\icons8-bar-chart-96.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.SetFocus()
        self.datSelect.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.datSelect_copy.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.Status.SetStatusWidths([-1])

        # statusbar fields
        Status_fields = ["frame_statusbar"]
        for i in range(len(Status_fields)):
            self.Status.SetStatusText(Status_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        static_line_3 = wx.StaticLine(self, wx.ID_ANY)
        static_line_3.SetBackgroundColour(wx.Colour(255, 255, 255))
        sizer_1.Add(static_line_3, 0, wx.EXPAND, 0)
        SelectDat = wx.StaticText(self, wx.ID_ANY, "Select .Dat file", style=wx.ALIGN_CENTER)
        sizer_1.Add(SelectDat, 0, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(self.datSelect, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        static_line_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        sizer_1.Add(static_line_1, 0, wx.EXPAND, 0)
        GenerateReport = wx.StaticText(self, wx.ID_ANY, "Generate report", style=wx.ALIGN_CENTER)
        sizer_1.Add(GenerateReport, 0, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(self.datSelect_copy, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_2, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def SelectDatFile(self, event):  # wxGlade: MyFrame.<event_handler>
    
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
    

    def GenerateReport(self, event):  # wxGlade: MyFrame.<event_handler>
        save = wx.SaveFileSelector('Report', '.pdf', 'Report.pdf')
        print(save, format(str))
        try:
            global datafiltered
            datafiltered = mdf.filtered_data(fileDir)
            datafiltered.to_csv(os.path.join(dirname, 'sortedList.csv'))
            print(dirname)
        except:
            print('Select correct file')
        
        try:
            rp = reportGen(datafiltered, 'IQR')
            rp.pptGenerator()
            # print('Successful!')
        except:
            print('Report gen unsuccessful')
        finally:
            event.Skip()
        
            
# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    ReportGen = MyApp(0)
    ReportGen.MainLoop()
