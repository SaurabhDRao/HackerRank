from math import floor, sqrt

t = int(input())
for i in range(t):
    l, h = [int(x) for x in input().split()]
    if(sqrt(l) - floor(sqrt(l)) == 0):
        print(floor(sqrt(h)) - floor(sqrt(l)) + 1)
    else:
        print(floor(sqrt(h)) - floor(sqrt(l)))