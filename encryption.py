from math import sqrt, floor, ceil

s = input()
l = len(s)
a = floor(sqrt(l))
b = ceil(sqrt(l))
if((a * b) < l):
    a += 1

el = []
si = 0
for i in range(a):
    t = []
    for j in range(b):
        try:
            t.append(s[si])
            si += 1
        except:
            break
    el.append(t)

for i in range(b):
    for j in range(a):
        try:
            print(el[j][i], end="")
        except:
            break
    print(" ", end="")