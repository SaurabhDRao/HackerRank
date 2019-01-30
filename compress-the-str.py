from itertools import groupby

s = input()
gList = [list(g) for k, g in groupby(s)]

for g in gList:
    print("(" + str(len(g)) + ", " + g[0] + ")", end = " ")