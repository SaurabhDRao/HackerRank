n, k = map(int, input().split())
a = [int(x) for x in input().split()]
pn = 1
sp = 0
for c in a:
    for i in range(1, c + 1):
        if(pn == i):
            sp += 1
        if(i % k == 0 and i != c):
            pn += 1
    pn += 1

print(sp)