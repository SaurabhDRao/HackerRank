key = int(input())
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
try:
    print(a.index(key))
except:
    print("-1")