from collections import OrderedDict

n = int(input())
od = OrderedDict()
for _ in range(n):
    w = input()
    if(w not in od):
        od[w] = 1
    else:
        od[w] += 1

print(len(od))
for d in od:
    print(od[d], end = " ")