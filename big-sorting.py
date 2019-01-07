n = int(input())
s = []
for i in range(n):
    s.append(input())

s.sort(key = int)
for x in s:
    print(x)