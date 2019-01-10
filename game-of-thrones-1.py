s = input()

d = {}
for c in s:
    if(c not in d):
        d[c] = 1
    else:
        d[c] += 1

l = [x for x in d.values()]
oc = [x for x in l if(x % 2 == 1)]
if(len(oc) > 1):
    print("NO")
else:
    print("YES")