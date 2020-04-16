from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from datetime import date
import pandas as pd
import os
import matplotlib.pyplot as plt
from pdfdocument.document import PDFDocument
from io import BytesIO
import seaborn as sns
from pdfdocument.document import colors
from pdfdocument.document import pdfmetrics
from pptx import Presentation

        
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

def generateFolders(df):
    for col in df.columns:
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), col))
        except FileExistsError:
            print('Oops! folder already exists')
            
            
def outlierTreatmentIQR(df, type = 'IQR'):
    if type == 'IQR':
        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)
        IQR = q3 - q1
        df_out = df[~((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR))).any(axis = 1)]
        print(df_out.shape)
        return df_out
        #os.path.join(os.path.dirname(__file__), 'Test fig of ' + col)
    if type == 'Zscore':
        pass
    

def plots(df):
    df = outlierTreatmentIQR(df, type = 'IQR')
    sns.distplot(df.iloc[:, 0])
    plt.savefig('After outlier treatment.png')
    

def pptGenerator(template):
    
    #DEFINE CONSTANTS
    TITLE_AND_SUBTITLE = 0
    CONTENT_SLIDE = 1
    
    #INITIALIZE PRESENTATION
    prs = Presentation(template)
    
    #LAYOUTS FOR SLIDES
    title_slide_layout = prs.slide_layouts[TITLE_AND_SUBTITLE]
    content_slide_layout = prs.slide_layouts[CONTENT_SLIDE]
    
    #ADD TITLE AND SUBTITLE SLIDE
    slide = prs.slides.add_slide(title_slide_layout)
    slide.placeholders[0].text = 'INCA - recording Report'
    slide.placeholders[1].text = str(date.today())

    #ADD CONTENT
    


    # for shape in slide.placeholders:
    #     print('%d %s' % (shape.placeholder_format.idx, shape.name))
    #     shape.text = 'This is text'
    
    prs.save('test.pptx')
    
#df = pd.read_csv('D:\Designing\Programming\PyCharm\MachineLearning\sortedList.csv', index_col = 0)

#plots(df)

ppt = pptGenerator('D:\Designing\Programming\PyCharm\MachineLearning/template.pptx')