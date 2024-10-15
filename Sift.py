import pandas as pd
import numpy as np

data = pd.read_csv('PreKnockout.csv')
arr = np.array(data)

res = []


def bfs(winner, n):
    q = [winner]
    count = 1
    while len(q):
        t = q.pop(0)
        for item in arr:
            if item[2] == n and item[-1] == t:
                q.append(item[4])
                q.append(item[5])
                print('ID:{}'.format(count))
                print('Stage:{}'.format(n))
                printfun(item)
                count += 1
                if count / n == 2:
                    n *= 2
                    break

    return


def printfun(item):
    res.append(item)
    print(" " * 36)
    print("Date:{} {}".format(item[0], item[3]))
    print("{:>15} VS {:<15}".format(item[4], item[5]))
    print("{:>15} : {:<15}".format(item[8], item[9]))
    if item[8] == item[9]:
        print("{:>15} : {:<15}".format(item[6], item[7]))
    print("\t\t  winner:{:27}".format(item[-1]))
    print(" " * 36)


def get_FST():
    fst = []
    for x in res[1:]:
        winner = x[-1]
        if winner not in fst:
            fst.append(winner)
    return fst[:3]


print('ID:0')
print('Stage:0')
printfun(arr[0])
bfs(arr[1][-1], 1)
pd.DataFrame(res).to_csv('sifted.csv', index=False, header=False)

fst = get_FST()
print('冠军:{:15}亚军:{:15}季军:{:15}'.format(fst[0],fst[1],fst[2]))
