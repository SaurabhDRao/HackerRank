n = int(input())
nl = []
ml = []
for i in range(n):
    line = [x for x in input().split()]
    ml.append([float(line[1]), float(line[2]), float(line[3])])
    nl.append(line[0])

name = input()
print("{0:.2f}".format(round((sum(ml[nl.index(name)]) / 3), 2)))