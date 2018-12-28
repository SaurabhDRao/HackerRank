n = int(input())
p = [int(x) for x in input().split()]

p.insert(0, 0)

for x in range(1, n + 1):
    t = p.index(x)
    print(p.index(t))