import pandas as pd

data = pd.read_csv('result.csv')

df = data.iloc[:, 1:]

columns = ['Round of 16',
           'Quarter-final',
           'Semi-final',
           'Play-off for third place',
           'Final']
# 提取出不同阶段的赛程
Round_of_16 = df[df['2'] == columns[0]]
Quarter_final = df[df['2'] == columns[1]]
Semi_final = df[df['2'] == columns[2]]
Play_off_for_third_place = df[df['2'] == columns[3]]
Final = df[df['2'] == columns[4]]
# 保存文件
Round_of_16.to_csv('Round_of_16.csv', index=False, header=False)
Quarter_final.to_csv('Quarter_final.csv', index=False, header=False)
Semi_final.to_csv('Semi_final.csv', index=False, header=False)
Play_off_for_third_place.to_csv('Play_off_for_third_place.csv', index=False, header=False)
Final.to_csv('Final.csv', index=False, header=False)
