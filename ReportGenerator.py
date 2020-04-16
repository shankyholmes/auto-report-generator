from datetime import date
import pandas as pd
import os
from io import BytesIO
from pptx import Presentation
from Plots import plots
from fuzzywuzzy import process

# def pdfGenerator(df = None):
#     c = canvas.Canvas('Engine test report.pdf', bottomup = 0, pagesize = A4)
#     c.setTitle('Engine test report')
#     c.translate(cm, cm)
#     c.drawCentredString(300, 50, 'Engine test Report')
#
#
#
#
#     c.showPage()
#     c.save()

# def generateFolders(df):
#     for col in df.columns:
#         try:
#             os.mkdir(os.path.join(os.path.dirname(__file__), col))
#         except FileExistsError:
#             print('Oops! folder already exists')

class reportGen():
    
    def __init__(self, df, outlierTreatment = 'IQR'):
        self.df = self.outlierTreatmentIQR(df, type = outlierTreatment)
        self.dirname = os.path.dirname(__file__)
    
    def outlierTreatmentIQR(self, df, type):
        if type == 'IQR':
            q1 = df.quantile(0.25)
            q3 = df.quantile(0.75)
            IQR = q3 - q1
            df_out = df[~((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR))).any(axis = 1)]
            print(df_out.shape)
            return df_out
            # os.path.join(os.path.dirname(__file__), 'Test fig of ' + col)
        if type == 'Zscore':
            pass
    
    def pptGenerator(self, template):
        df1 = self.df
        
        # DEFINE CONSTANTS
        TITLE_AND_SUBTITLE = 0
        CONTENT_SLIDE = 1

        # INITIALIZE PRESENTATION
        prs = Presentation(template)

        # LAYOUTS FOR SLIDES
        title_slide_layout = prs.slide_layouts[TITLE_AND_SUBTITLE]
        content_slide_layout = prs.slide_layouts[CONTENT_SLIDE]

        # ADD TITLE AND SUBTITLE SLIDE
        slide = prs.slides.add_slide(title_slide_layout)
        slide.placeholders[0].text = 'INCA - recording Report'
        slide.placeholders[1].text = 'Generated on {:%m-%d-%Y}'.format(date.today())
        
        # ADD CONTENT
        
        #ADD JOINTPLOT FOR QSET
        slide = prs.slides.add_slide(content_slide_layout)
        
        slide.placeholders[22].text = '22'
        slide.placeholders[16].text = '1'

        slide.placeholders[23].text = '23'
        slide.placeholders[17].text = '17'

        # scatter for qset and speed
        QSET = process.extractOne('InjCtl_qSetUnBal', df1.columns)[0]
        print(QSET)
        SPEED = process.extractOne('Epm_nEng', df1.columns)[0]
        print(SPEED)
        plots.scatterplot(plots, df1[SPEED], df1[QSET])
        print(os.path.join(self.dirname, 'scatterplot.png'))
        slide.placeholders[24].insert_picture(os.path.join(self.dirname, 'scatterplot.png'))
        slide.placeholders[20].text = 'Qset and Speed scatter'

        slide.placeholders[25].text = '25'
        slide.placeholders[21].text = '21'
        
        
        # #ADD OTHER PLOTS
        # for col in df1.columns:
        #     slide = prs.slides.add_slide(content_slide_layout)
        #
        #     plots.distplot(plots, df[col])
        #     # plots.scatterplot(plots, df[col])
        #
            
            
            
            
            
        
        
        
        
        slide = prs.slides.add_slide(content_slide_layout)
        
        for shape in slide.placeholders:
            print('%d %s' % (shape.placeholder_format.idx, shape.name))

        prs.save('test.pptx')


df = pd.read_csv('D:\Designing\Programming\PyCharm\MachineLearning\sortedList.csv', index_col = 0)

ppt = reportGen(df).pptGenerator('D:\Designing\Programming\PyCharm\MachineLearning/template.pptx')