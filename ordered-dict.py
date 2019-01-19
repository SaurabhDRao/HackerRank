from collections import OrderedDict

n = int(input())
od = OrderedDict()
for _ in range(n):
    line = input().split()
    intemEnd = len(line) - 1
    item = " ".join(line[0 : intemEnd])
    cost = int(line[intemEnd])
    if(item not in od):
        od[item] = cost
    else:
        od[item] += cost

for d in od:
    print(d, od[d])