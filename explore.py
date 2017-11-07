import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm


def drawLinePlotByAttr(df, attr, showFig=True):
    y = df.groupby(attr).mean().Sales
    x = range(1, len(y)+1)
    plt.plot(x, y, 'o-')

    # annotate figure
    plt.xlabel(attr)
    plt.ylabel("Average Sales")
    plt.title("Average Sales VS {}".format(attr))
    plt.grid(True)
    if len(y) < 35:
        for a, b in zip(x, y):
            plt.text(a, b, str(int(b)))
        if attr == 'YearMonth':
            plt.xticks(x, y.index.values.tolist(), rotation='vertical')
        else:
            plt.xticks(x, y.index.values.tolist())

    # save figure
    plt.savefig("./img/{}Average.png".format(attr[0].lower() + attr[1:]))
    if showFig is True:
        plt.show()
    plt.close()


def drawBarByAttr(df, attr, showValue=True, showFig=True, isCount=False):

    if isCount:
        keywords = 'Count'
        y = df.groupby(attr).size()
    else:
        keywords = 'MeanSales'
        y = df.groupby(attr).mean().Sales

    x = y.index.values.tolist()

    # draw figures
    if len(x) < 40:
        for i in range(0, len(x)):
            plt.bar(i, y[i], color=cm.jet(1. * i / len(x)), tick_label=x[i])
            plt.xticks(range(len(x)), x)
    else:
        plt.bar(range(len(x)), y)

    # annotate figures
    plt.xlabel(attr)
    plt.ylabel(keywords)
    plt.title("{} VS {}".format(keywords, attr))

    if showValue is True:
        for a, b in zip(range(len(x)), y):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

        # save figure
    plt.savefig("./img/{}{}.png".format(attr[0].lower() + attr[1:], keywords))

    if showFig is True:
        plt.show()
    plt.close()





train_clean = pd.read_csv('./data/trainCleaned.csv')
test_clean = pd.read_csv('./data/testCleaned.csv')

# draw line plots
for attr in ['Month', 'Year', 'Day', 'DayOfWeek', 'WeekOfYear', 'YearMonth']:
    drawLinePlotByAttr(train_clean, attr, showFig=True)

# draw bar plots
for attr in ['StoreType', 'Assortment', 'StateHoliday', 'SchoolHoliday', 'Store']:
    if attr not in ['Store']:
        drawBarByAttr(train_clean, attr, showFig=True)
        drawBarByAttr(train_clean, attr, showFig=True, isCount=True)
    else:
        drawBarByAttr(train_clean, attr, showValue=False, showFig=True)

