import seaborn as sns
import matplotlib.pyplot as plt




class plots():
    
    def distplot(self, df):
        
        sns.set(style = "whitegrid", palette = "muted", color_codes = True)
        f, axes = plt.subplots(1, 1, figsize = (5.97, 2.63))
        sns.distplot(df, hist = True, bins = 100, kde_kws = {'shade': True}, ax = axes)
        
        plt.savefig('distplot.png')
    
    def scatterplot(self, dfx, dfy):
        sns.set(style = "whitegrid", palette = "muted", color_codes = True)
        f, axes = plt.subplots(1, 1, figsize = (5.97, 2.63))
        sns.scatterplot(dfx, dfy, ax = axes)
        plt.savefig('scatterplot.png')
        
    def jointplot(self, dfx, dfy):
        sns.jointplot(dfx, dfy)
        plt.savefig('jointplot.png')
        
    def kdejointplot(self, dfx, dfy):
        f, axes = plt.subplots(1, 1, figsize = (5.97, 2.63))
        sns.jointplot(dfx,dfy, kind = 'kde', height = 3, space = 0)