def buildMap(l):
    d = {}
    for e in l:
        if(e not in d):
            d[e] = 1
        else:
            d[e] += 1
    return d

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]

d1 = buildMap(a)
diff = []
if(len(list(set(b).difference(a))) != 0):
    diff = list(set(b).difference(a))
d2 = buildMap([x for x in b if(x not in diff)])

for x in d1:
    if(d1[x] != d2[x]):
        diff.append(x)

print(" ".join([str(x) for x in sorted(diff)]))