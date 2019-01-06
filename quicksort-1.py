n = int(input())
a = [int(x) for x in input().split()]
p = a[0]
l = []
r = []
e = [p]
for i in range(1, n):
    if(a[i] > p):
        r.append(a[i])
    elif(a[i] < p):
        l.append(a[i])
    else:
        e.append(a[i])

for x in l:
    print(x, end = " ")
for x in e:
    print(x, end = " ")
for x in r:
    print(x, end = " ")