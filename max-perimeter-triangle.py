from itertools import combinations

n = int(input())
a = sorted([int(x) for x in input().split()])

combs = combinations(a, 3)
maxp = -1
sides = []
for c in list(combs):
    if((c[0] + c[1] > c[2]) and (c[0] + c[2] > c[1]) and (c[1] + c[2] > c[0])):
        p = c[0] + c[1] + c[2]
        if(p > maxp):
            maxp = p
            sides = [c[0], c[1], c[2]]

if(maxp == -1):
    print("-1")
else:
    print(" ".join([str(x) for x in sides]))