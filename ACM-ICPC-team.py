n, m = [int(x) for x in input().split()]
l = []
for i in range(n):
    l.append(input())

t = []
for i in range(n):
    count = 0
    for j in range(i + 1, n):
        n1 = int(l[i], 2)
        n2 = int(l[j], 2)
        o = n1 | n2
        o1 = "{0:b}".format(o)
        count = o1.count("1")
        t.append(count)

print(max(t), t.count(max(t)), sep="\n")
    