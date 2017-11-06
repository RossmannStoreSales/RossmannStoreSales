import pandas as pd
import matplotlib.pyplot as plt


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


def drawBarByAttr(df, attr, showValue=True, showFig=True):
    y = df.groupby(attr).mean().Sales
    x = y.index.values.tolist()

    # draw figures
    plt.bar(range(len(x)), y, tick_label=x)

    # annotate figures
    plt.xticks(range(len(x)), x)
    plt.xlabel(attr)
    plt.ylabel("Average Sales")
    plt.title("Average Sales VS {}".format(attr))

    if showValue is True:
        for a, b in zip(range(len(x)), y):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

        # save figure
    plt.savefig("./img/{}Average.png".format(attr[0].lower() + attr[1:]))

    if showFig is True:
        plt.show()
    plt.close()


train_clean = pd.read_csv('./data/trainCleaned.csv')
test_clean = pd.read_csv('./data/testCleaned.csv')

for attr in ['Month', 'Year', 'Day', 'DayOfWeek', 'WeekOfYear', 'YearMonth']:
    drawLinePlotByAttr(train_clean, attr, showFig=True)


# for attr in ['StoreType', 'Assortment', 'StateHoliday', 'SchoolHoliday', 'Store']:
#     if attr not in ['Store']:
#         drawBarByAttr(train_clean, attr, showFig=True)
#     else:
#         drawBarByAttr(train_clean, attr, showValue=False, showFig=True)

