n = int(input())
l = [int(x) for x in input().split()]

d=[]
for x in l:
    diff = (len(l) - 1 - l[::-1].index(x)) - l.index(x)
    if(diff > 0):
        d.append(diff)

if len(d)==0:
    print('-1')
else:
    print(min(d))