from datetime import date
# import pandas as pd
import os
import numpy as np
from pptx import Presentation
import Plots as plots
from fuzzywuzzy import process
from scipy import stats


# import seaborn as sns


class reportGen():
    
    def __init__(self, df, treatment_type = 'IQR'):
        self.df = self.outlierTreatmentIQR(df, type = treatment_type)
        self.dirname = os.path.dirname(__file__)
    
    def outlierTreatmentIQR(self, df, type):
        
        # IQR BASED OUTLIER TREATMENT
        if type == 'IQR':
            q1 = df.quantile(0.25)
            q3 = df.quantile(0.75)
            IQR = q3 - q1
            df_out = df[~((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR))).any(axis = 1)]
            return df_out
        
        # ZSCORE BASED OUTLIER TREATMENT
        if type == 'Zscore':
            z = np.abs(stats.zscore(df))
            threshold = 2
            df_out = df[(z < threshold).all(axis = 1)]
            return df_out
    
    def pptGenerator(self):
        df1 = self.df
        template = os.path.join(self.dirname, 'template.pptx')
        
        
        # DEFINE CONSTANTS
        TITLE_AND_SUBTITLE = 0
        CONTENT_SLIDE_1 = 1
        CONTENT_SLIDE_2 = 2
        
        # INITIALIZE PRESENTATION
        prs = Presentation(template)
        
        # LAYOUTS FOR SLIDES
        title_slide_layout = prs.slide_layouts[TITLE_AND_SUBTITLE]
        content_slide_layout_1 = prs.slide_layouts[CONTENT_SLIDE_1]
        content_slide_layout_2 = prs.slide_layouts[CONTENT_SLIDE_2]
        
        # ADD TITLE AND SUBTITLE SLIDE
        slide = prs.slides.add_slide(title_slide_layout)
        slide.placeholders[0].text = 'INCA - recording Report'
        slide.placeholders[1].text = 'Generated on {:%m-%d-%Y}'.format(date.today())
        
        # ADD CONTENT

        # ADD JOINTPLOT FOR QSET
        slide = prs.slides.add_slide(content_slide_layout_2)
        
        # extracting label names
        QSET = process.extractOne('InjCtl_qSetUnBal', df1.columns)[0]
        SPEED = process.extractOne('Epm_nEng', df1.columns)[0]
        
        # top left
        slide.placeholders[22].insert_picture('scatterplot.png')
        slide.placeholders[16].text = '1'
        
        # top right
        plots.jointplot(df1[SPEED], df1[QSET])
        slide.placeholders[23].insert_picture('jointplot.png')
        slide.placeholders[17].text = 'Zone mapping of the data w.r.t Qset and Speed'
        
        # bottom left
        # scatter for qset and speed
        # plots.scatterplot(df1[SPEED], df1[QSET])
        slide.placeholders[24].insert_picture('scatterplot.png')
        slide.placeholders[20].text = 'Qset and Speed scatter'
        
        # #ADD OTHER PLOTS
        # for col in df1.columns:
        #     slide = prs.slides.add_slide(content_slide_layout_1)
        #
        #     plots.distplot(plots, df[col])
        #     # plots.scatterplot(plots, df[col])
        # top left
        # slide.placeholders[22].insert_picture('scatterplot.png')
        # slide.placeholders[16].text = '1'
        #
        # # top right
        #
        # slide.placeholders[23].insert_picture('scatterplot.png')
        # slide.placeholders[17].text = '17'
        #
        # # bottom left
        # # scatter for qset and speed
        # QSET = process.extractOne('InjCtl_qSetUnBal', df1.columns)[0]
        # SPEED = process.extractOne('Epm_nEng', df1.columns)[0]
        # plots.scatterplot(plots, df1[SPEED], df1[QSET])
        # slide.placeholders[24].insert_picture(os.path.join(self.dirname, 'scatterplot.png'))
        # slide.placeholders[20].text = 'Qset and Speed scatter'
        #
        # # bottom right
        # plots.jointplot(plots, df1[SPEED], df1[QSET])
        # slide.placeholders[25].insert_picture('jointplot.png')
        # slide.placeholders[21].text = 'Jointplot for Qset and Speed'
        
        # for shape in slide.placeholders:
        #     print('%d %s' % (shape.placeholder_format.idx, shape.name))
        
        prs.save('Report.pptx')


# df = pd.read_csv('D:\Designing\Programming\PyCharm\MachineLearning\sortedList.csv', index_col = 0)
#
# ppt = reportGen(df, 'IQR').pptGenerator()