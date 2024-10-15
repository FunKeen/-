import pandas as pd
import numpy as np

data = pd.read_csv('Knockout.csv')
pd.set_option('future.no_silent_downcasting', True)

data.replace('Play-off for third place', 0, inplace=True)
data.replace('Final', 1, inplace=True)
data.replace('Semi-final', 2, inplace=True)
data.replace('Quarter-final', 4, inplace=True)
data.replace('Round of 16', 8, inplace=True)

arr = np.array(data)
arr = sorted(arr, key=lambda y: y[2])


def winner(item):
    re = item[4]
    if item[8] < item[9] or item[8] == item[9] and item[6][1] < item[7][1]:
        re = item[5]
    return re


for x in arr:
    x[-1] = winner(x)

pd.DataFrame(arr).to_csv('PreKnockout.csv', index=False)
