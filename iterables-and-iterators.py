from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

count = 0
cl = list(combinations(l, k))

for c in cl:
    if('a' not in c):
        count += 1

print("{0:.3f}".format(1 - (count / len(cl))))