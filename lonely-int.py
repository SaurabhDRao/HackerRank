n = int(input())
a = [int(x) for x in input().split()]

d = {}
for c in a:
    if(c not in d):
        d[c] = 1
    else:
        d[c] += 1

for c in d:
    if(d[c] == 1):
        print(c)
        break