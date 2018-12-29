n = int(input())
nl = []
sl = []
for i in range(n):
    name = input()
    score = float(input())
    nl.append(name)
    sl.append(score)

s = set(sl)
s.discard(min(s))
m = min(s)
sec = []
for i in range(n):
    if(sl[i] == m):
       sec.append(nl[i]) 

sec.sort()
for x in sec:
    print(x)