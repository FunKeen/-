import pandas as pd

data = pd.read_csv('result.csv')

df = data.iloc[:, 1:]

columns = ['Round of 16',
           'Quarter-final',
           'Semi-final',
           'Play-off for third place',
           'Final']


# 提取出不同阶段的赛程

def select(df):
    # 筛选
    Group = df[-df['2'].isin(columns)]
    Knockout = df[df['2'].isin(columns)]

    # 保存文件
    Group.to_csv('Group.csv', index=False)
    Knockout.to_csv('Knockout.csv', index=False)


select(df)
