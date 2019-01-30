n, k = [int(x) for x in input().split()]
l = []
for _ in range(k):
    t = [float(x) for x in input().split()]
    l.append(t)

grp = list(zip(*l))

for g in grp:
    print(sum(g) / k)