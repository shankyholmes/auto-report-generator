import seaborn as sns
import matplotlib.pyplot as plt


def distplot(df):
    sns.set(style = "whitegrid", palette = "muted", color_codes = True)
    f, axes = plt.subplots(1, 1, figsize = (5.97, 2.63))
    sns.distplot(df, hist = True, bins = 100, kde_kws = {'shade': True}, ax = axes)
    plt.savefig('distplot.png')


def scatterplot(dfx, dfy):
    sns.set(style = "whitegrid", palette = "muted", color_codes = True)
    f, axes = plt.subplots(1, 1, figsize = (5.97, 2.63))
    sns.scatterplot(dfx, dfy, ax = axes, marker = '+')
    plt.savefig('scatterplot.png')


def jointplot(dfx, dfy):
    sns.jointplot(x = dfx, y = dfy, kind = 'kde', space = 0, height = 6.15, color = 'g')
    plt.savefig('jointplot.png')
